function submitData(){
    var name = $('#name').val();
    var surname = $('#surname').val();
    var birthdate = $('#birthdate').val();

    jsonObject={
        "Id":"",
        "Name":"",
        "Surname":"",
        "BirthDate":"",
    }
    jsonObject.Id=ID_Generator(name,surname);
    jsonObject.Name = name;
    jsonObject.Surname = surname;
    jsonObject.BirthDate = birthdate; 
    console.log(jsonObject);

    exportToJsonFile(jsonObject);
}

function ID_Generator(Name, Surname){
	var val = Math.floor(1000 + Math.random() * 9000);
	var ID = Name[0].toLowerCase() + Surname[0].toLowerCase() + val;
	return ID
}
  

function exportToJsonFile(jsonData) {
    let dataStr = JSON.stringify(jsonData);
    let dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
    
    let exportFileDefaultName = 'riders.json';
    
    let linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click(); 
    }

    

