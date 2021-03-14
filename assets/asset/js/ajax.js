// ON LOAD CURSORE FOCUSE

// KEY PRESS VALIDATION //////
function OnlyLetterKey(evt)
{	
	var charCode = (evt.which) ? evt.which : event.keyCode
	 
	if ((charCode == 34) || (charCode == 27) || (charCode > 32 && charCode < 37) || 
		(charCode > 37 && charCode < 46) ||
	 
		(charCode > 46 && charCode < 65) || (charCode > 90 && charCode < 97) || (charCode > 122 && charCode < 127))

         return false;
''}

function OnlyNumberKey(evt)
{	
	var charCode = (evt.which) ? evt.which : event.keyCode
	
	if ((charCode < 48 || charCode > 57) && (charCode !== 8) && (charCode !== 9) && (charCode !== 46))
	
         return false;
}

function AllKey(evt)
{	
	var charCode = (evt.which) ? evt.which : event.keyCode
	if ((charCode == 34) || (charCode == 39))
	 return false;
}



//sub_catagory
function nationality()
{	
	var country_id = document.getElementById("country_id").value;
	
	var xmlRequest = GetXmlHttpObject();
	if (xmlRequest == null)
    return;
	
		var url="registration/nationality/"+country_id;
		
    	var browser=navigator.appName;
		if (browser=="Microsoft Internet Explorer")
		{
			xmlRequest.open("POST",url, true);
		}
		else
		{
			xmlRequest.open("GET",url, true);
		}
		
		xmlRequest.setRequestHeader("Content-Type", "application/x-www-formurlencoded");
		xmlRequest.onreadystatechange =function()
		{
			if(xmlRequest.readyState==4)
			{
				HandleAjaxResponse_nationality(xmlRequest);
			}
		};
			xmlRequest.send(null);
			return false;
}

function HandleAjaxResponse_nationality(xmlRequest)
{
	var xmlT = xmlRequest.responseText;
	document.getElementById('nationality').innerHTML = xmlT;
}


//total_collection_report
function add_size_view()
{	
	var add_view = document.getElementById("add_view").value;

	var xmlRequest = GetXmlHttpObject();
	if (xmlRequest == null)
    return;			
	
		var url="addManage/add_size_view/"+add_view;
		
    	var browser=navigator.appName;
		if (browser=="Microsoft Internet Explorer")
		{
			xmlRequest.open("POST",url, true);
		}
		else
		{
			xmlRequest.open("GET",url, true);
		}
		
		xmlRequest.setRequestHeader("Content-Type", "application/x-www-formurlencoded");
		xmlRequest.onreadystatechange =function()
		{
			if(xmlRequest.readyState==4)
			{
				HandleAjaxResponse_add_size_view(xmlRequest);
			}
		};
			xmlRequest.send(null);
			return false;
}

function HandleAjaxResponse_add_size_view(xmlRequest)
{
	var xmlT = xmlRequest.responseText;
	document.getElementById('add_size_view_show').innerHTML = xmlT;
}


/////////////////// OBJECT FUNCTION ////////////////////////
	function GetXmlHttpObject()
  	{		
		var xmlHttp=null;
		try
		{
         	xmlHttp=new XMLHttpRequest();
        }
		catch (e)
		{
        	// Internet Explorer
            try
            {
            	xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
             catch (e)
             {
              	xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
             }
        }
		return xmlHttp;		  
    } 
