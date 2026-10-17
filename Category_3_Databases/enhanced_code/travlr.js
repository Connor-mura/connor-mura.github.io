const mongoose = require('mongoose');

// Define the trip schema, with validation limits and parameter trimming
const tripSchema = new mongoose.Schema({ 
    code: { type: String, required: [true, 'Trip code required'], index: true, unique: true, trim: true, uppercase: true, match: [/^[A-Z0-9]{4,10}$/, 'Must be alphnumeric and between 4-10 characters'] }, 
    name: { type: String, required: [true, 'Trip name required'], index: true, trim: true, maxlength: [100, 'Trip name cannot exceed 100 characters'] }, 
    length: { type: Number, required: [true, 'Trip duration required'], min: [1, 'Trip must be at least one day'] }, 
    start: { type: Date, required: [true, 'Trip start date required'] }, 
    resort: { type: String, required: [true, 'Trip destination required'], trim: true }, 
    perPerson: { type: Number, required: [true, 'Per person rates required'], min: [0, 'Price cannot be negative'] },   
    image: { type: String, required: [true, 'Image path required'], trim: true }, 
    description: { type: String, required: [true, 'Trip description required'], maxlength: [1000, 'Trip description cannot exceed 1000 characters'] } 
}); 
const Trip = mongoose.model('trips', tripSchema); 
module.exports = Trip; 