from confluent_kafka import Consumer, KafkaException, KafkaError

# Kafka 配置
conf = {
    'bootstrap.servers': '172.16.14.16:9092',  # Kafka broker 地址
    'group.id': 'my_group',                 # 消费者组
    'auto.offset.reset': 'latest'         # 从最早的消息开始读取
}

# 创建消费者实例
consumer = Consumer(conf)

# 订阅主题
consumer.subscribe(['forecast'])

if __name__=="__main__":
# 消费消息
    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # 超时时间为 1 秒

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # 已经到达分区结尾
                    print('Reached end at offset %d' % msg.offset())
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                # 打印消息内容
                print('Received message: %s' % msg.value().decode('utf-8'))

    except KeyboardInterrupt:
        pass
    finally:
        # 关闭消费者
        consumer.close()
