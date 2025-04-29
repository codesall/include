import org.apache.spark.sql.SparkSession

object PrimeNumberCheck {
  def main(args: Array[String]): Unit = {

    // Step 1: Initialize SparkSession
    val spark = SparkSession.builder()
      .appName("Prime Number Check")
      .master("local[*]")  // Use all available cores
      .getOrCreate()

    // Step 2: List of numbers to check for primality
    val numbers = List(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

    // Step 3: Parallelize the list using Spark
    val rdd = spark.sparkContext.parallelize(numbers)

    // Step 4: Check each number for primality
    val resultRDD = rdd.map { num =>
      val isPrime = if (num < 2) false
      else (2 until num).forall(x => num % x != 0)

      if (isPrime) s"$num is Prime" else s"$num is Not Prime"
    }

    // Step 5: Collect and print results
    resultRDD.collect().foreach(println)

    // Step 6: Stop Spark session
    spark.stop()
  }
}
