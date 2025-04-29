import org.apache.spark.sql.SparkSession

object SparkCalculator {
  def main(args: Array[String]): Unit = {

    // Step 1: Initialize SparkSession
    val spark = SparkSession.builder()
      .appName("Spark Calculator")
      .master("local[*]") // Use all available cores
      .getOrCreate()

    // Step 2: Sample list of tuples (number1, number2)
    val numberPairs = List((10, 2), (7, 0), (5, 3), (12, 4))

    // Step 3: Parallelize data using RDD
    val rdd = spark.sparkContext.parallelize(numberPairs)

    // Step 4: Perform operations
    val resultRDD = rdd.map { case (a, b) =>
      val add = a + b
      val sub = a - b
      val mul = a * b
      val div = if (b != 0) a.toDouble / b else "undefined (division by zero)"
      
      s"For numbers ($a, $b): Add = $add, Sub = $sub, Mul = $mul, Div = $div"
    }

    // Step 5: Show results
    resultRDD.collect().foreach(println)

    // Step 6: Stop Spark
    spark.stop()
  }
}
