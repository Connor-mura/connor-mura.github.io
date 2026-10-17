// Connor_Mura_CS499_Artifact_One.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>
#include <string>
#include "Models.h"
#include "CrudUtility.h"

int main() {
	//Instantiates generic class utility using AnimalRecord struct
	CrudUtility<AnimalRecord> shelterEngine;


	//TEST CREATE OPERATIONS
	AnimalRecord animalOne{ "A0001", "Frank", "Golden Retriever" };
	AnimalRecord animalTwo{ "A0002", "Lilly", "Pug" };
	AnimalRecord animalThree{ "A0003", "Bella", "Cat" };

	//Calls createRecord method
	shelterEngine.createRecord(animalOne);
	shelterEngine.createRecord(animalTwo);
	shelterEngine.createRecord(animalThree);

	//Calls database count method
	std::cout << "Current database size: " << shelterEngine.count() << "\n\n";


	//TEST READ OPERATIONS
	std::vector<AnimalRecord> pugResults = shelterEngine.readRecords([](const AnimalRecord& record) {
		return record.breed == "Pug";
		});

	for (const auto& item : pugResults) {
		std::cout << "Animal ID: " << item.animalId
			<< " | Name: " << item.name
			<< " | Breed: " << item.breed << "\n";
	}
	

	//TEST UPDATE OPERATIONS
	int updateRecordsCount = shelterEngine.updateRecords(
		[](const AnimalRecord& record) { return record.name == "Frank"; },
		[](AnimalRecord& record) { record.name = "Air Bud"; }
	);
	std::cout << "Total rows modified: " << updateRecordsCount << "\n\n";


	//TEST DELETE OPERATIONS
	int deletedRecordsCount = shelterEngine.deleteRecords([](const AnimalRecord& record) {
		return record.animalId == "A0003";
		});
	//Calls database count method
	std::cout << "Current database size: " << shelterEngine.count() << "\n\n";

	return 0;
}
