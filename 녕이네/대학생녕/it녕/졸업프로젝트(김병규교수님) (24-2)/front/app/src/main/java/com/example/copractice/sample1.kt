package com.example.copractice

fun main() {
forAndWhile( )
    //3. String Template
//    val name = "Wendy"
//    val lastName = "Choi"
//    println("My name is ${name + lastName} I'm 23")
//    println("Is this true? ${1==0}")
//    println("This is 2\$a")
//
    /*
    *
    *
    */
}

//4. 조건식
fun maxBy(a : Int, b : Int) : Int{
    if(a > b){
        return a
    }else{
        return b
    }
}

fun maxBy2(a : Int, b : Int) : Int = if(a>b) a else b

fun checkNum(score : Int) : Unit {
    when(score) {
        0 -> println("this is 0")
        1 -> println("this is 1")
        2,3 -> println("this is 2 or 3")
        else -> println("I don't know")
    }

    var b : Int = when(score) {
        1 -> 1
        2 -> 2
        else -> 3
    }

    println("b : ${b}")

    when(score){
        in 90..100 -> println("You are genius")
        in 10..80 -> println("Not bad")
        else -> println("Okay")
    }

}

// Expression vs Statement

// 5. Array and List

// Array

// List 1. List(수정 가능) 2. MutableList(수정 불가)

fun array(){
    val array = arrayOf(1, 2, 3)
    val list :List<Int> = listOf(1, 2, 3)

    val array2 : Array<Any> = arrayOf(1, "d", 3.4f)
    val list2 : List<Any> = listOf(1, "d", 11L)

    array[0] = 3
    var result = list.get(0)

    var arrayList :ArrayList<Int> = arrayListOf<Int>()
    arrayList.add(10)
    arrayList.add(20) // lista listB
    arrayList[0] == 20

}

// 6. For / While

fun forAndWhile(){
    val students :ArrayList<String> = arrayListOf("Wendy", "Jennie", "James", "Jennifer")

    for ( name : String in students) {
        println("${name}")
    }
    var sum : Int = 0
    for ( i in 1..10){
        sum += 1
    }
    println(sum)
}


//1. 함수

fun helloWorld() : Unit {
    println("Hello World!")
}

fun add(a : Int, b : Int) : Int { //여기서는 int 생략 x (무언가를 return 하게 되면 return 타입 지정해줘야함)
    return a+b
}

//2. val vs var
// val = value

fun hi(){
    val a : Int = 10 //변할 수 없는 값

    var b : Int = 9 //변할 수 있는 값

    b = 100

    val c = 100 //val c : Int = 100 (이렇게 Int 생략해줘도 됨, val/var 구분은 하기)
    var d = 100
    var name : String = "Wendy"


}