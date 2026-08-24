fun main() {
    for (c in 1..readLine()!!.toInt()) {
        val n = readLine()!!.toInt()
        var p = 0
        for (m in 2..100000) {
            if (n % m == 0) {
                p = m
                break
            }
        }
        if (p == 0) {
            p = n
        }
        println("${n / p} ${n - (n / p)}")
    }
}