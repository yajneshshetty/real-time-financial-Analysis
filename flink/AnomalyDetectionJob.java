
import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import java.util.Properties;

public class AnomalyDetectionJob {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        Properties properties = new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG, "financial-group");

        FlinkKafkaConsumer<String> kafkaConsumer = new FlinkKafkaConsumer<>("financial_transactions", new SimpleStringSchema(), properties);
        DataStream<String> stream = env.addSource(kafkaConsumer);
        stream.print();
        env.execute("Anomaly Detection Job");
    }
}
