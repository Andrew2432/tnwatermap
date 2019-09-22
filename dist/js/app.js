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

function getSelectedMap() {
	let year = getSelectedYear();
	let month = getSelectedMonth();

	new_year = String(year);
	new_month = String(month);
	new_year_short = String(new_year).substring(2, 4);
	base_address = "water_data/img/";
	new_address = `${base_address}${new_year}/avwl_${new_month}${new_year_short}.png`;

	console.log(new_address);

	imgTag = document.getElementById("map");
	document.getElementById("map").setAttribute("src", new_address);
}
