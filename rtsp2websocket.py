import asyncio
import websockets
import cv2


cap = cv2.VideoCapture('ipcam-url')

async def accept(websocket, path):
    while True:
        try:
            ret, frame = cap.read()
            
            encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
            _ ,imgencode = cv2.imencode('.jpg', frame, encode_param)

            await websocket.send(imgencode.tobytes())
        except:
            pass



start_server = websockets.serve(accept, '', 9997)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()