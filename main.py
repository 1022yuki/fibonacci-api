from fastapi import FastAPI
import sys
sys.setrecursionlimit(10**8)

app = FastAPI()

@app.get("/fib")
def getFib(n: int):
    global fibList
    fibList = [-1]*(n+1)
    return {"result": fib(n)}

# フィボナッチ数列の第n項を返す関数
def fib(n: int) -> int:
    global fibList
    if n == 1 or n == 2:
        return 1
    if fibList[n] != -1:
        return fibList[n]
    else:
        fibList[n] = fib(n-1) + fib(n-2)
        return fibList[n]