// PrimeCheck.scala
object PrimeCheck {
  def main(args: Array[String]): Unit = {
    val number = scala.io.StdIn.readInt()
    val isPrime = if (number <= 1) false else (2 until number).forall(x => number % x != 0)
    if (isPrime) println(s"$number is Prime") else println(s"$number is NOT Prime")
  }
}
