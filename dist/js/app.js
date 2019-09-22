function getSelectedYear() {
	let year = document.getElementById("year");
	let selectedYear = year.options[year.selectedIndex].value;
	return selectedYear;
}

function getSelectedMonth() {
	let month = document.getElementById("month");
	let selectedMonth = month.options[month.selectedIndex].value;
	return selectedMonth;
}

function doesFileExist(urlToFile) {
	var xhr = new XMLHttpRequest();
	xhr.open("HEAD", urlToFile, false);
	xhr.send();

	if (xhr.status == "404") {
		return false;
	} else {
		return true;
	}
}

function getSelectedMap() {
	let year = getSelectedYear();
	let month = getSelectedMonth();

	new_year = String(year);
	new_month = String(month);
	new_year_short = String(new_year).substring(2, 4);

	base_address = "water_data/img/";
	base_csv_address = "water_data/csv/";
	default_address = "water_data/img/2011/avwl_Mar11.webp";
	new_address = `${base_address}${new_year}/avwl_${new_month}${new_year_short}.webp`;
	new_csv_address = `${base_csv_address}${new_year}/avwl_${new_month}${new_year_short}.csv`;

	// Check if image file exists, else use default file
	url_new_address = `http://127.0.0.1:5501/${new_address}`;
	//url_new_address = `https://tnwatermap.netlify.com/${new_address}`;
	isURL = doesFileExist(url_new_address);

	if (isURL) {
		set_address = new_address;
		plotTable(new_csv_address);
	} else {
		set_address = default_address;
		alert("Proper data not available");
	}
	//console.log(set_address);
	imgTag = document.getElementById("map");
	document.getElementById("map").setAttribute("src", set_address);
}

function plotTable(address) {
	d3.text(address, function(data) {
		var parsedCSV = d3.csv.parseRows(data);

		var container = d3
			.select("#table-data")
			.append("table")

			.selectAll("tr")
			.data(parsedCSV)
			.enter()
			.append("tr")

			.selectAll("td")
			.data(function(d) {
				return d;
			})
			.enter()
			.append("td")
			.text(function(d) {
				return d;
			});
	});
}
