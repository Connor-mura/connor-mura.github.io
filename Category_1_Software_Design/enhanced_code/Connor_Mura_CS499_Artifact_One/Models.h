#pragma once
#include <string>

//Example model 1: Original Animal Shelter Records
struct AnimalRecord {
	std::string animalId;
	std::string name;
	std::string breed;

	//helper method for identification
	std::string getId() const { return animalId; }
};

//Example model 2: Logistics Records
struct LogisticsRecord {
	std::string trackingId;
	std::string destination;
	double weight;
	std::string status;

	//helper method
	std::string getId() const { return trackingId; }
};
