object HelloWorld {
  def main(args: Array[String]): Unit = {
    val num1 = scala.io.StdIn.readDouble()
    val num2 = scala.io.StdIn.readDouble()
    val op = scala.io.StdIn.readLine()

    val result = op match {
      case "+" => (num1 + num2).toString
      case "-" => (num1 - num2).toString
      case "*" => (num1 * num2).toString
      case "/" => if (num2 != 0) (num1 / num2).toString else "Cannot divide by zero"
      case _   => "Invalid operation"
    }

    println(s"Result: $result")
  }
}
