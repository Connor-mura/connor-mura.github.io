#pragma once
#include <vector>
#include <algorithm>
#include <optional>
#include <functional>

//userData can be AnimalRecord, LogisticsRecord, or any custom struct/class
template <typename userData>
class CrudUtility {
private:
	std::vector<userData> database; //Fully decoupled internal storage container

public:
	//CREATE: Safely appends any record type passed by reference
	bool createRecord(const userData& record) {
		if (record.getId().empty()) return false;

		database.push_back(record);
		return true;
	}

	//READ: Accepts a custom function to dynamically filter fields
	std::vector<userData> readRecords(std::function<bool(const userData&)> predicate) const {
		std::vector<userData> results;
		for (const auto& record : database) {
			if (predicate(record)) {
				results.push_back(record);
			}
		}
		return results;
	}

	//UPDATE: Finds matching records via filter and updates them via modifier function
	int updateRecords(std::function<bool(const userData&)> predicate, std::function<void(userData&)> modifier) {
		int modifiedCount = 0;
		for (auto& record : database) {
			if (predicate(record)) {
				modifier(record);
				modifiedCount++;
			}
		}
		return modifiedCount;
	}

	//DELETE: Leverages vector erase and explicit iterators cleanly
	int deleteRecords(std::function<bool(const userData&)> predicate) {
		auto initialSize = database.size();

		database.erase(
			std::remove_if(database.begin(), database.end(), predicate),
			database.end()
		);

		return static_cast<int>(initialSize - database.size());
	}

	//Helper to get total database size
	size_t count() const { return database.size(); }
};
