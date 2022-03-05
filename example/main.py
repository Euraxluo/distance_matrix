# -*- coding: utf-8 -*-
# Time: 2022-02-28 14:47
# Copyright (c) 2022
# author: Euraxluo

from fastapi import FastAPI


from dot_matrix import dot_matrix_router

app = FastAPI(
    title="DotMatrix",
    description="DotMatrix is use AMap api  build points matrix",
)
app.include_router(dot_matrix_router)  # 增删改





if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host="localhost", port=5000, debug=True)