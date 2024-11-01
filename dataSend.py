
import pandas as pd
import time
import json
from confluent_kafka import Producer
from sympy.codegen import While


def getDfData(filePath):
    df = pd.read_csv(filePath, delim_whitespace=True, header=None)
    df.columns = ['station', 'forecastTime', 'shortwaveIrrad', 'scatterIrrad', 'directIrrad', 'windSpeed', 'windDir', 'tmp', 'rh', 'surfacePres']
    return df

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def sendKafkaData(df):
    # 设置 Kafka 配置
    conf = {
        'bootstrap.servers': '172.16.14.16:9092',  # 替换为你的Kafka Broker地址
    }



    dataJson = df.to_dict(orient='records')
    topic = 'station_weather'
    producer = Producer(**conf)
    for data in dataJson:
        # data["forecastTime"] = int(time.time() * 1000)
        dataStr = json.dumps(data)
        producer.produce(topic, key="data", value=dataStr, callback=delivery_report)

    # 等待所有消息被发送
        producer.flush()
        print("发送数据" + dataStr)
        time.sleep(2)

if __name__ == "__main__":
    while True:
        df = getDfData("./data/ynyb-sun-2024090600.txt")
        sendKafkaData(df)