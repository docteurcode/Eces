let words =[];

function addDebourreInfo(){
    let debourreAdd = document.getElementById('debourreInput').Value;
    if(debourreAdd!=''){
        word.push(debourreAdd)
    }
}

function showdebourreInfo(){
    let showInfo ="";
    let counter = 0;
    words.forEach(name =>
        showInfo+=  <tr>
                        <td>${name}</td>
                        <td>${name}</td>
                        <td>${name}</td>
                        <td>${name}</td>
                        <td><button type="button" class="btn btn-block btn-danger" value="${counter++}"  onclick="removeDebourre(this)">supprimer</button> </td>
                    </tr> 
        )
    document.getElementById('display').innerHTML = showInfo;
    document.getElementById('debourreInput').Value = null;
}

function removeDebourre(){    
    word.slice(parseInt(btnvalue.value), 1);
    showInfo(); 
}