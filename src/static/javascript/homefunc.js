function getTicketInfo(ticket){
  let allTickets = "alltickets";
  let token = getCookie("csrftoken");
  console.log("test");

  $.ajax(
    {
        headers: { "X-CSRFToken": token },
        type:"POST",
        url: "/getticket/",
        data:{
                 "ticketNum": ticket,
        },
        success: function( response ) 
        {
          let ticketTable = document.getElementById("ticketDiv");
          let jsonReturn = JSON.parse(response);
          ticketTable.innerHTML = "";
          for(var i = 0; i < jsonReturn.length; i++) {
            var obj = jsonReturn[i];
            ticketTable.innerHTML += "<p>Ticket Number: " + obj.ticketNum + " - " + obj.title + "</p>";
            ticketTable.innerHTML += "<p>Assigned: " + obj.is_assigned +"</p>";
            ticketTable.innerHTML += "<p>Priority: " + obj.priority +"</p>";
            ticketTable.innerHTML += "<p>Date Created: " + obj.date_created + "</p>";
            ticketTable.innerHTML += "<p>Due Date: " + obj.due_date + "</p>";
            ticketTable.innerHTML += "<p>Last Checked: " + obj.last_checked + "</p>";
            ticketTable.innerHTML += "<p>Date Closed: " + obj.date_closed + "</p>";
            ticketTable.innerHTML += "<p>Description: " + obj.description + "</p>";
        }


        }
      }
  )
}

function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
}

function AllTickets(){
  let allTickets = "alltickets";
  let token = getCookie("csrftoken");
  console.log("test");

  $.ajax(
    {
        headers: { "X-CSRFToken": token },
        type:"POST",
        url: "/searchticket/",
        data:{
                 "alltickets": allTickets,
        },
        success: function( response ) 
        {
          BuildTable(response)
          let searchTicket = document.getElementById("ticketSearch");
          let status = document.getElementsByName("status")[0];
          let priority = document.getElementsByName("priority")[0];
          let assigned = document.getElementsByName("assigned")[0];

          status.value = "A";
          priority.value = "A";
          assigned.value = "A";
          searchTicket.value = "";

          console.log(status)
        }
      }
  )
  
}
function MyTickets(){
  let myTickets = "mytickets";
  let token = getCookie("csrftoken");

  $.ajax(
    {
        headers: { "X-CSRFToken": token },
        type:"POST",
        url: "/searchticket/",
        data:{
                 "mytickets": myTickets,
        },
        success: function( response ) 
        {
          BuildTable(response)
          let searchTicket = document.getElementById("ticketSearch");
          let status = document.getElementsByName("status")[0];
          let priority = document.getElementsByName("priority")[0];
          let assigned = document.getElementsByName("assigned")[0];

          status.value = "A";
          priority.value = "A";
          assigned.value = "A";
          searchTicket.value = "";

          console.log(status)
        }
      }
  )


}

function  TicketSearch(){

  let searchTicket = document.getElementById("ticketSearch");
  let status = document.getElementsByName("status")[0];
  let priority = document.getElementsByName("priority")[0];
  let assigned = document.getElementsByName("assigned")[0];
  console.log(status.value, priority.value, assigned.value)
  let token = getCookie("csrftoken");
  $.ajax(
    {
        headers: { "X-CSRFToken": token },
        type:"POST",
        url: "/searchticket/",
        data:{
                 post_id: searchTicket.value,
                 "status": status.value,
                 "priority": priority.value,
                 "assigned": assigned.value,
        },
        success: function( response ) 
        {
          BuildTable(response)
        }
      }
  )
}
function BuildTable(response){
          let jsonReturn = JSON.parse(response);
          let ticketTable = document.getElementById("ticketDiv");
          let status;
          let assigned;
          let priority;
          let mark;
          let innerHtml = '';
          if (jsonReturn.length == 0){
            innerHtml = "<h1><a href='#'> No Tickets Found</h1>"
          }
          for (var i = 0; i < jsonReturn.length; i++) 
          { 
            let ticketDiv = '<div onclick="getTicketInfo(' + jsonReturn[i]["ticketNum"] + ')" class="ticketInfo"><h3 class="subTicketHeaders">' + jsonReturn[i]["ticketNum"] + ' - ' + jsonReturn[i]["title"] + '</h3>';
            if (jsonReturn[i]["status"] == "O"){
              status = "Open";
            }else{''
              status = "Closed";
            }
            ticketDiv += '<h4 class="subTicketHeaders">Status: ' + status + '</h4>'
            if (jsonReturn[i]["priority"] == "R"){
              priority = "Routine";
            }else if(jsonReturn[i]["priority"] == "U"){
              priority = "Urgent"
            }else{
              priority = "Emergency"
            }
             ticketDiv += '<h4 class="' + jsonReturn[i]["priority"] + '">Priority: ' + priority + '</h4>'
             if (jsonReturn[i]["is_assigned"] == true){
              assigned = "True";
              mark = "&#x2713;"
            }else{
              assigned = "False"
              mark = "&#x2715;"
            }

            ticketDiv += '<h4 class="subTicketHeaders">Assigned:<p class="assigned'+assigned+'">' + mark +'</p></h4><p class="ticketP">Creation Date: ' + jsonReturn[i]["date_created"] +'</p><p class="ticketP">Due Date:' + jsonReturn[i]["due_date"] + '</p><p class="ticketP">Last Checked:' + jsonReturn[i]["last_checked"] + '</p></div>'
            innerHtml += ticketDiv;
          }
          ticketTable.innerHTML = innerHtml;

}
