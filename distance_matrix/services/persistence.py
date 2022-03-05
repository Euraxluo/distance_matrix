# -*- coding: utf-8 -*- 
# Time: 2022-03-03 18:49
# Copyright (c) 2022
# author: Euraxluo


from distance_matrix.schemas.persistence import *
from distance_matrix.services.dishashing import *

from sqlalchemy.dialects.mysql import insert
from sqlalchemy import text

register.orm_base.metadata.create_all(bind=register.orm_engine, checkfirst=True)


def create(*edges: EdgeUpsert):
    with register.orm() as db:
        db.bulk_insert_mappings(EdgeORM, [e.orm_create() for e in edges])
        db.commit()


def edge_persistence():
    with register.orm() as db:
        data = []
        for k, f, v in edge_list():
            _, start, end = k.split(':')
            data_item = EdgeUpsert(start=start, end=end, **json.loads(v))
            if data_item.distance == 0:
                continue
            data.append(data_item.dict())
        try:
            upsert(db, EdgeORM, data)
        except Exception as e:
            register.logger.error(f"Edge Persistence Error:{e},data_len:{len(data)},data:{data[0]}")


def upsert(session, model: EdgeORM, rows: List[dict], batch_size: int = 200):
    table = model.__table__
    update_cols = [c.name for c in table.c
                   if c not in list(table.primary_key.columns)]

    for idx in [(i, i + batch_size) for i in range(0, len(rows), batch_size)]:
        tmp_rows = rows[idx[0]:idx[1]]
        insert_stmt = insert(table).values(tmp_rows)

        on_duplicate_stmt = insert_stmt.on_duplicate_key_update(
            **{k: getattr(insert_stmt.inserted, k) if k != "update_at" else text('CURRENT_TIMESTAMP') for k in update_cols},
        )
        session.execute(on_duplicate_stmt)
        session.commit()
