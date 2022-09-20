const express = require('express')
const app = express()

app.use(express.json())

app.get('', (req,res) => {
    res.send('Hello World')
})

app.post('/find_area',(req,res) => {
    let length = req.body.length
    let breadth = req.body.breadth
    let area = length * breadth
    res.json({
        'area' : area
    })

})

let notes = [{"id":1,"msg":"veg"}]

app.get('/get_notes', (req,res) => {
    res.send(notes)
})

app.post('/add_notes',(req,res) => {
    let message = req.body.message
    let pre_id = notes[notes.length-1].id
    let new_note = {
        "id" : pre_id+1,
        "message" : message
    }
    notes.push(new_note)
    res.send("post Notes successfully")

})

app.delete('/delete_note/:id',(req,res) => {
    let id = parseInt(req.params.id)
    let new_notes = notes.filter((note) => note.id !== id)
    notes = new_notes
    res.send("delete Notes successfully")

})

app.listen(3000, (req,res) => {
    console.log('server run')
})