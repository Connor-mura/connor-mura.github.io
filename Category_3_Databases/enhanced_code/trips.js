const mongoose = require('mongoose');
const Trip = require('../models/travlr'); //Register model
const Model = mongoose.model('trips');

// Whitelist regular expression pattern for sanitation
const ALPHA_NUM_PATTERN = /^[A-Z0-9]{4,10}$/;

//GET: /trips - lists all the trips
//Regardless of outcome, response must include HTML status code
// and JSON message to the requesting client
const tripsList = async(req, res) => {
    try {
        const q = await Model
            .find({}) //No filter, return all records
            .exec();

            //Uncomment the following line to show results of query
            //on the console
            //console.log(q);

        if(!q || q.length === 0)
        { //Database returned no data
            return res
                .status(404)
                .json(err);
        } else { //Return resulting trip list
            return res
                .status(200)
                .json(q);
        }
    } catch (err) {
        return res
            .status(500)
            .json({ "error": "database read failure", "details": err.message });
    }

};

//GET: /trips/:tripCode - lists a single trip
//Regardless of outcome, response must include HTML status code
// and JSON message to the requesting client
const tripsFindByCode = async(req, res) => {
    try {
        const targetCode = req.params.tripCode ? req.params.tripCode.toUpperCase().trim() : '';

        //input validation to prevent injection attacks
        if (!ALPHA_NUM_PATTERN.test(targetCode)) {
            return res
                .status(400)
                .json({ "message": "invalid trip code format"});
        }

        const q = await Model
            .find({'code' : targetCode }) // Return single record
            .exec();

            //Uncomment the following line to show results of query
            //on the console
            //console.log(q);

        if(!q || q.length === 0)
        { //Database returned no data
            return res
                .status(404)
                .json(err);
        } else { //Return resulting trip list
            return res
                .status(200)
                .json(q);
        }
    } catch (err) {
        return res
            .status(500)
            .json({ "status": "database failure", "error": err.message});
    }

};

//POST: /trips - Adds a new Trip
// Regardless of outcome, response must include HTML status code
// and JSON message to the requesting client
const tripsAddTrip = async(req, res) => {
    try {

        // Verification checks
        if (Number(req.body.length) <= 0 || Number(req.body.perPerson) < 0) {
            return res
                .status(400)
                .json({ "message": "entry invalid"});
        }

        const newTrip = new Trip({
            code: req.body.code,
            name: req.body.name,
            length: req.body.length,
            start: req.body.start,
            resort: req.body.resort,
            perPerson: req.body.perPerson,
            image: req.body.image,
            description: req.body.description
        });

        const q = await newTrip.save();

        if(!q)
        {
        //Database returns no data
            return res
                .status(400)
                .json(err);
        } else { //return new trip
            return res
                .status(201)
                .json(q);
        }
        //uncomment the following line to show results of operation on the console
        //console.loq(q);
    } catch (err) {
        return res
            .status(400)
            .json({ "status": "database failure", "error": err.message });
    }
};

// PUT: /trips/:tripCode - Adds a new Trip 
// Regardless of outcome, response must include HTML status code 
// and JSON message to the requesting client 
const tripsUpdateTrip = async(req, res) => { 
 
    // Uncomment for debugging 
    //console.log(req.params); 
    //console.log(req.body); 
    try {

        const targetCode = req.params.tripCode ? req.params.tripCode.toUpperCase().trim() : '';

        // Param safety check
        if (!ALPHA_NUM_PATTERN.test(targetCode)) {
            return res
                .status(400)
                .json({ "message": "Invalid code"});
        }

        //boundry check
        if (Number(req.body.length) <= 0 || Number(req.body.perPerson) < 0) {
            return res
                .status(400)
                .json({ "message": "Input invalid"});
        }

        const q = await Model 
            .findOneAndUpdate( 
                { 'code' : req.params.tripCode }, 
                { 
                    code: req.body.code, 
                    name: req.body.name, 
                    length: req.body.length, 
                    start: req.body.start, 
                    resort: req.body.resort, 
                    perPerson: req.body.perPerson, 
                    image: req.body.image, 
                    description: req.body.description 
                },
                { new: true, runValidators: true } 
            ) 
        .exec(); 
         
        if(!q) 
        { // Database returned no data 
            return res 
                .status(400) 
                .json(err);
        } else { // Return resulting updated trip 
            return res 
                .status(201) 
                .json(q); 
        }     
                
        // Uncomment the following line to show results of operation 
        // on the console 
        // console.log(q);
    } catch (err) {
        return res
            .status(500)
            .json({ "status": "database failure", "error": err.message});
    } 
};

module.exports = {
    tripsList,
    tripsFindByCode,
    tripsAddTrip,
    tripsUpdateTrip
};