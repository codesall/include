object HelloWorld {
	def main(args: Array[String]): Unit = {
        val number = scala.io.StdIn.readInt()
        if (number > 0) println(s"$number is Positive")
        else if (number < 0) println(s"$number is Negative")
        else println(s"$number is Zero")
    }
}