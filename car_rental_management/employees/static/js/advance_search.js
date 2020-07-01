var advance_condition_names = ['first_category', 'second_category', 'third_category', 'fourth_category', 'fifth_category'];
var advance_condition_values = ['first_condition', 'second_condition', 'third_condition', 'fourth_condition', 'fifth_condition'];
var advance_connection = ['first_connection', 'second_connection', 'third_connection', 'fourth_connection', 'fifth_connection'];
var condition_counter = 0;

function toggle_element(element) {
	if (element == null)
		return;
	
	if (element.style.display == "none") {
		if (element.id.includes("date_group")) {
			element.style.display = "flex";
		}
		else {
			element.style.display = "block";
		}
	} else {
		element.style.display = "none";
	}
}

function hideGeneralSearch() {
	var general = document.getElementById("basic_general");
	var advance = document.getElementById("div_advance"); 
	var btn_ad = document.getElementById("btn_advance");
	var btn_new_condition = document.getElementById("btn_new_condition");
	var btn_clear = document.getElementById("btn_clear");
	
	var date_group = document.getElementById("date_group");
	var label_date = document.getElementById("label_date");	
	var date_group_pickup = document.getElementById("date_group_pickup");
	var label_date_pickup = document.getElementById("label_date_pickup");
	var date_group_return = document.getElementById("date_group_return");
	var label_date_return = document.getElementById("label_date_return");
	
	var div_order = document.getElementById("div_order");


	toggle_element(general);
	toggle_element(advance);
	toggle_element(btn_ad);
	toggle_element(btn_new_condition);
	toggle_element(btn_clear);

	toggle_element(date_group);
	toggle_element(label_date);
	toggle_element(date_group_pickup);
	toggle_element(label_date_pickup);
	toggle_element(date_group_return);
	toggle_element(label_date_return);
	
	toggle_element(div_order);
}

function remove_conditions() {
	var parent = document.getElementById("div_advance");
	//document.getElementById("btn_advance").disabled = true;
	while (parent.firstChild) {
		parent.removeChild(parent.firstChild);
	}
	condition_counter = 0;
}

function create(htmlStr) {
	var frag = document.createDocumentFragment(),
		temp = document.createElement('div');
	temp.innerHTML = htmlStr;
	while (temp.firstChild) {
		frag.appendChild(temp.firstChild);
	}
	return frag;
}