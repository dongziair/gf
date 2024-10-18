
import asyncio
import websockets

async def websocket_client():
    uri = "http://localhost:8005/ws/topic/message"  # 服务器的WebSocket地址
    async with websockets.connect(uri) as websocket:
        while True:
            # 接收来自服务器的消息
            message = await websocket.recv()
            print(f"Received message: {message}")

# 启动WebSocket客户端
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(websocket_client())
