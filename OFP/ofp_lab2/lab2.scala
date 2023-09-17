import scala.util.matching.Regex


val represent_short: Short => String = x=> rsl(x.toInt, List(), 16)
val rsl : (Int, List[Int], Int) => String = {
    case (_, bits, 0) => bits mkString ""
    case (num, bits, counter) => rsl(num>>1, (num&1) :: bits, counter-1)
}

val get_sign_and_abs_part: (String) => (Boolean, String) = 
    str => {
        val num_pattern = """^\s*-0*([1-9][0-9]*)\s*$|
                                |^\s*-?(0+)\s*$|
                                |^\s*\+?(0+)\s*$|
                                |^\s*\+?0*([1-9][0-9]*)\s*$""".r
        num_pattern.findFirstMatchIn(str) match{
            case None => (false, null)
            case Some(value) => value.subgroups match {//.filter(x=>x != null)(0)
                case x::_ if x != null => (false, x)
                case _::x::_ if x != null => (true, "0") 
                case _::_::x::_ if x != null => (true, "0")
                case _::_::_::x::_ if x != null => (true, x)
                case _ => (false, null)
            }
        }
    }
val str_to_ints : (String) => List[Int] = 
    str => str.toCharArray().toList.map(x=>x-48)


val devide_by_2: List[Int] => List[Int] = lst => strip_left_zeros(db2l(lst.reverse, Nil))
val strip_left_zeros: List[Int] => List[Int] = {
    case 0::rest => strip_left_zeros(rest)
    case x::rest => x::rest
    case Nil => List(0)
}
val db2l: (List[Int], List[Int]) => List[Int] = {
    case (x :: x_rest, Nil) => db2l(x_rest, x/2 :: Nil)
    case (Nil, x) => x
    case (x :: Nil, y :: result_rest) => x/2 :: (y+(x%2)*5) :: result_rest
    case (x :: x_rest, y :: result_rest) => db2l(x_rest, x/2 :: y+(x%2)*5 :: result_rest)
}


val dec_digits_to_binary: List[Int] => List[Short] = ints => ddtbl(ints.reverse, Nil)
val ddtbl: (List[Int], List[Int]) => List[Short] = {
    case (List(0), Nil) => List(0)
    case (List(0), bits) => bits.map(x => x.toShort).toList
    case (x::x_rest, bits) => ddtbl(devide_by_2(((x-x%2)::x_rest).reverse).reverse, x%2::bits)
    case (_, x) => List(0)
}


val binary_short_digits_to_five_shorts: List[Short] => List[Short] =
    x => bsdtfsl(x, List(0,0,0,0,0))
val bsdtfsl: (List[Short], List[Short]) => List[Short] = {
    case (Nil, result) => result
    case (b :: bs, result) => bsdtfsl(bs, append_bit_to_list_of_shorts(b, result))
}
val append_bit_to_list_of_shorts: (Short, List[Short]) => List[Short] = 
    (bit, lst) => {
        // println("+++")
        // print("Изначальный список ")
        // println(lst.map(x => represent_short(x)))

        var shifted = lst.map(x => (x<<1).toShort)
        // print("Сдвинули всё влево на 1 ")
        // println(shifted.map(x => represent_short(x)))

        var to_add = lst.map(x => (if (x >= 0)  0 else 1).toShort).tail.appended(bit)
        // print("Битики для добавления ")
        // println(to_add.map(x => x.toBinaryString))

        var res = shifted.zip(to_add).map(
            x => (x._1 | x._2).toShort
        )
        // print("Получилось ")
        // println(res.map(x => represent_short(x)))
        // println("+++")
        res
    }

val invert_fives: List[Short] => List[Short] = 
    lst => lst.map(x => (~x).toShort)

val add_fivess: (List[Short], List[Short]) => List[Short] = 
    (a,b) => afl(a.reverse,b.reverse,false,Nil)
val afl: (List[Short], List[Short], Boolean, List[Short]) => List[Short] = {
    case (Nil, Nil, _, res) => res
    case (a::as, b::bs, false, res) => afl(as, bs, check_overfill(a.toShort, b.toShort), (a+b).toShort::res)
    case (a::as, b::bs, true, res) => afl(
        as, bs, 
        check_overfill(a.toShort,b.toShort) |  check_overfill((a+b).toShort, 1), 
        (a+b+1).toShort::res)
    case (_,_,_,res) => res
}

val check_overfill: (Short, Short) => Boolean = 
    (x,y) => col(short_to_bits(x).reverse,short_to_bits(y).reverse,0,16)
val col: (List[Int], List[Int], Int, Int) => Boolean = {
        case (x,y,z,0) => z >= 1
        case (x::xs,y::ys,z,counter) => {
            col(
                xs, ys, if ((x+y+z) > 1) 1 else 0, counter-1
            )
        }
        case (_,_,_,_) => true
    }

val short_to_bits: Short => List[Int] = x=> stbl(x.toInt, List(), 16)
val stbl : (Int, List[Int], Int) => List[Int] = {
    case (_, bits, 0) => bits
    case (num, bits, counter) => stbl(num>>1, (num&1) :: bits, counter-1)
}

val mult_fives: (List[Short], List[Short]) => List[Short] = 
    (xlist, ylist) => mfl(
        xlist, 
        ylist.map(short_to_bits).flatten.reverse,
        List(0,0,0,0,0),
    ) 
val mfl: (List[Short], List[Int], List[Short]) => List[Short] = {
    case (_, Nil, result) => result
    case (xlist, bit::bits, result) if (bit == 1) => mfl(
            append_bit_to_list_of_shorts(0, xlist),
            bits,
            add_fivess(result, xlist)
        )
    case (xlist, bit::bits, result) => mfl(
        append_bit_to_list_of_shorts(0, xlist),
        bits,
        result
    )
}


val string_to_fivess: (String) => List[Short] = str => {
    var (sign, abs) = get_sign_and_abs_part(str)
    var fivess = binary_short_digits_to_five_shorts(
        dec_digits_to_binary(
            str_to_ints(abs)
        )
    )
    // ставим первый бит в 0
    fivess = (fivess.head & 65535).toShort :: fivess.tail
    if (!sign) 
        fivess = (new MyLong(invert_fives(fivess)) + new MyLong("1")).fivess 
    fivess
}


class MyLong(lst: List[Short]){
    var fivess : List[Short] = lst

    def this() = this(List(0.toShort,0.toShort,0.toShort,0.toShort,0.toShort))
    def this(s: String) = this(string_to_fivess(s))
    
    def +(that: MyLong): MyLong = {
        new MyLong(add_fivess(this.fivess, that.fivess))
    }

    def unary_-() = new MyLong(invert_fives(this.fivess)) + new MyLong("1")

    def signum() : Int = if (this.fivess.head.toShort >= 0) 1 else -1

    def -(that: MyLong): MyLong = new MyLong(add_fivess(this.fivess, (-that).fivess))

    def *(that: MyLong): MyLong = {
        var sign = this.signum() * that.signum()
        var abs1 = if(this.signum() == 1) this.fivess else (-this).fivess
        var abs2 = if(that.signum() == 1) that.fivess else (-that).fivess

        var abs_res = mult_fives(abs1, abs2)
        if (sign == 1) new MyLong(abs_res) else - new MyLong(abs_res)

    }

    override def toString(): String = this.fivess map(represent_short) mkString ""
}



var a = new MyLong("-12")
var b = new MyLong("327")
var c = a * b
println(c.fivess)
println((-c).fivess)
