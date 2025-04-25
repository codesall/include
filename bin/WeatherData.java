import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;

public class WeatherData {

    public static class WeatherMapper extends Mapper<Object, Text, Text, DoubleWritable> {
        private Text category = new Text();
        private DoubleWritable value = new DoubleWritable();

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String line = value.toString();
            String[] fields = line.split("\\s+");

            if (fields.length > 3) {
                try {
                    // Assuming columns: [Temperature DewPoint WindSpeed]
                    double temperature = Double.parseDouble(fields[0]);
                    double dewPoint = Double.parseDouble(fields[1]);
                    double windSpeed = Double.parseDouble(fields[2]);

                    category.set("Temperature");
                    value.set(temperature);
                    context.write(category, value);

                    category.set("DewPoint");
                    value.set(dewPoint);
                    context.write(category, value);

                    category.set("WindSpeed");
                    value.set(windSpeed);
                    context.write(category, value);

                } catch (NumberFormatException e) {
                    // Skip invalid lines
                }
            }
        }
    }

    public static class WeatherReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {
        private DoubleWritable result = new DoubleWritable();

        public void reduce(Text key, Iterable<DoubleWritable> values, Context context) throws IOException, InterruptedException {
            double sum = 0;
            int count = 0;

            for (DoubleWritable val : values) {
                sum += val.get();
                count++;
            }

            double average = sum / count;
            result.set(average);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Weather Data Average");
        job.setJarByClass(WeatherData.class);
        job.setMapperClass(WeatherMapper.class);
        job.setCombinerClass(WeatherReducer.class);
        job.setReducerClass(WeatherReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(DoubleWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
