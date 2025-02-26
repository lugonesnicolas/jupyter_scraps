import json
import requests
from pathlib import Path

def main():
    headers_path = Path("A:/BeOn_Repositories/headers_peyapp.json")
    url = "https://mobile-api.pedidosya.com/mobile/v8/functions/appInit?app=android&hash="

    payload = "{}"
    headers = {
    'accept-encoding': 'gzip',
    'baggage': 'sentry-environment=production,sentry-public_key=aa27ec0b39de46e3ad47971be7ad0fba,sentry-release=9.5.6.1,sentry-trace_id=43ac91b3e93e471a90febd2fa1ba575a',
    'connection': 'Keep-Alive',
    'content-type': 'application/json; charset=UTF-8',
    'host': 'mobile-api.pedidosya.com',
    'origin': 'PedidosYa',
    'peya-app-origin': 'splash',
    'peya-app-platform': 'android',
    'peya-app-version': '9.5.6.1',
    'peya-device-id': 'db9283feb4cf6855',
    'peya-global-entity-id': 'PY_ar',
    'peya-os-version': '34',
    'peya-performance-class': 'LOW_END',
    'peya-perseus-client-id': '1725396040934.581078583217633963.h3fngIeUIf',
    'peya-perseus-hitmatch-id': '1739549144987.787605655056730508.j0rnT6wFgC',
    'peya-perseus-sdk-version': '3.6.0',
    'peya-perseus-session-id': '1739546356664.484436555189973438.wl6o33UN4c',
    'peya-screen-dpi': '3',
    'peya-session-id': '0bd661ff-b01c-430f-b3f0-0a309117a276',
    'peya-session-timestamp': '1739546356664',
    'peya-trace-id': 'bba62074-719f-481b-bba1-ec3a68894345',
    'peya-whitelabel-id': 'com.pedidosya',
    'sentry-trace': '43ac91b3e93e471a90febd2fa1ba575a-0795e3798fb94804',
    'user-agent': 'google',
    'x-px-authorization': '3:2603e61c637525cda045713f83a9487a2cb390c3733ff315f6904862e48cedb8:VFoBmX5ovaKBd/SlzaYjOgyFLed70LY/7GcoHUc5UwqTx5lAzfD96p0aj8BLYg8pljfo3fjuvLiNFV7up6gV2Q==:1000:Rlp60+2i0HsAoIx18yay7w5PACl+VCYpezcbDRlzR0yRWSrFz+yQzdOLa+ygTiC6GZNPthI4f0qFh2HJftIOewXSBPWGBnXa4d3NRiiXcAzV5s0dyZm4SuNWP36oZitJjdb6mlcpWRHULKD5ZeAUV6rR+KWaJyYNZpiE9a9ut3E+hKEtrbzc6gWiD5h7DxSk7DpuVBwMa9Ij57GIKY8rmoIr7rAgMdAmNwD44ofGJz8=',
    'x-px-device-fp': 'db9283feb4cf6855',
    'x-px-device-model': 'sdk_gphone64_x86_64',
    'x-px-mobile-sdk-version': '3.3.0',
    'x-px-os': 'Android',
    'x-px-os-version': '14',
    'x-px-uuid': '8ba2689f-eaed-11ef-b1d3-ff8bfd35b811',
    'x-px-vid': 'c6d92520-6a34-11ef-8ad2-498b7336ef21',
    'x-trace-id': '0bd661ff-b01c-430f-b3f0-0a309117a276',
    'Cookie': '__cf_bm=QS019.rtnHAYZnU4R8IN6oHpEy2jL4d1RHA9uchv1gE-1739549239-1.0.1.1-0dqSXWxUUqgHJ7gb1YV4.n6c6U.whFRclwRspPC9N.M3Go99WWQbyZvkOO8WFQ4PdMsTx2cqzrwtjCRYV1hltg; _pxhd=8cd2b46c37c513ac99a9a6e92ae08d52f3f98dea2e300a31cbf1e7d356a4ce46:c6d92520-6a34-11ef-8ad2-498b7336ef21'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()

    new_app_token = response.get("LoginSystemResult", "").get("APIToken", "")


    # 1️⃣ Cargar el JSON desde un archivo (si está en un archivo)
    with headers_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
        
    # 3️⃣ Iterar sobre "PR" y "SCH" para modificar el campo "authorization"
    for key in ["PR", "SCH"]:
        if key in data.get("Pedidos Ya APP", {}):
            data["Pedidos Ya APP"][key]["headers"]["authorization"] = new_app_token
            
    # 4️⃣ Guardar el JSON modificado en un nuevo archivo
    with headers_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"JSON modificado y guardado en {headers_path}\nToken: {new_app_token}")
    
if __name__ == "__main__":
    main()