var name="Prasad Phadke"
console.log(name)
let last="Phadke";
last="Sharmna";
console.log(last)
let color;
console.log(color)
let colors=null
console.log(colors)
last=4;
last="Phd"
console.log(typeof(last))
// object
let car ={
    name:"Bugati",
    price:3000
}

car.name="BMW";
car.price=5000;



console.log(car.price)

// array

cars=['BMW','TATA',"JAGUAR"]
cars[2]=20

console.log(cars)

// function

function new_func(n,p) {
    console.log("this is " + n + " function");
    console.log("this is "+p+" function")
}

new_func('first','last')


function square(num) {
    return num*num
}

let number=square(3)
console.log(number)


// OOPS in JS

function createCircle(r) {
    return {
        r,
        d: function(r){
            k=r*r
            console.log(k)
        }
    }
}

const circle =createCircle(2)

console.log(circle)

