const app = Vue.createApp({
//template:` 
 //<h1> Hola Soy el mas Guapo </h1>
 //<p> {{ 5 - 4 }} </p>
//`
data(){
    return{
        message:'Este es un mensaje Hola world',
        quote: 'I am Spiderman',
        author: 'Bruce Parker'
    }
},
methods:{
    cambioQuoate( evento){
        console.log('Presione el Boton cambio', evento)
        this.author = "Antonio Barrios"
        this.capitalize()
    },
    capitalize(){
        this.quote = this.quote.toUpperCase()
    }
}

})

app.mount('#myApp')