//The body mass index (BMI) is a value derived from the mass (w) and height (l) of a person. 
//The BMI is defined as the body mass divided by the square of the body height, and is universally

function BMI(weight, height){
    // calculates the BMI where 
    //weight is in kg and height in meteres

    return weight*10000 / height**2
}


console.log(BMI(60, 174))
console.log(BMI(120, 180))
