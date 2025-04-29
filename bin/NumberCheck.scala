import org.apache.spark.sql.SparkSession

object NumberCheck {
  def main(args: Array[String]): Unit = {
    // Step 1: Create SparkSession
    val spark = SparkSession.builder()
      .appName("Number Check")
      .master("local[*]") // Run locally with all cores
      .getOrCreate()

    // Step 2: Input list of numbers (you can modify or get input dynamically)
    val numbers = List(10, -5, 0, 42, -8)

    // Step 3: Parallelize the list using Spark
    val rdd = spark.sparkContext.parallelize(numbers)

    // Step 4: Map each number to its type (positive, negative, or zero)
    val resultRDD = rdd.map { num =>
      if (num > 0) s"$num is Positive"
      else if (num < 0) s"$num is Negative"
      else s"$num is Zero"
    }

    // Step 5: Collect and print results
    resultRDD.collect().foreach(println)

    // Step 6: Stop Spark session
    spark.stop()
  }
}
