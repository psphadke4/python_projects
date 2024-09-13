t=[2,3,6,6,5]

const sorted_nums = [...new Set(t)].sort((a,b)=> b-a)[1]
console.log(sorted_nums)

k="1234"
k=123


try {
    let reversed = k.split('').reverse().join('')
    console.log(reversed)
    }
    catch(error) {
        console.log(error.message)
    }
    
class test {
    constructor(sides) {
        this.sides=sides
    }

    peri() {
        let sumall=0
        for (let side of this.sides) {
            sumall+=side

        }
        return sumall
    }
}

const sumit= new test([1,2,3,4])

console.log(sumit.peri())