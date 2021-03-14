
	$(window).ready(function(){
		
        /// INITIATE FILE UPLOAD
        if($('.attachmentbody').length > 0) {            
    		initiateFileUpload();
        }

        /// FILE REMOVE
		$('.attachmentbody').on('click', '.remove', function(){
            var el = $(this).parents('.attachmentbody').html('<div class="progress"><div class="progress-bar progress-bar-success progress-bar-striped active" style="width: 100%"></div></div>');
            $.ajax({
                url: URL.getSiteAction('upload/remove/'+el.attr("data-type")),
                type: "POST",
                dataType: "html",
                data: {attachment:$(el.attr("data-target")).val()},
                complete: function () {
                    $(el.attr("data-target")).val("");
                    el.html('<img class="upload" src="'+URL.getBaseAction('resource/img/no_image.png')+'" />');

                    reInitiateFileUpload(el);
                }
            });
        });

	});

	function initiateFileUpload() {
        $.each($(document).find('.attachmentbody'), function(i, el) {
            el = $(el);

            if(el.find('.upload').length > 0) {
                new AjaxUpload(el.find('.upload'), {
                    action: URL.getSiteAction('upload/index/'+el.attr("data-type")),
                    name: 'attachment',
                    responseType: 'json',
                    onSubmit: function(file, ext){
                        
                        if (! (ext && /^(jpg|png|jpeg|gif)$/.test(ext))){ 
                        // extension is not allowed
                                status.text('Only JPG, PNG or GIF files are allowed');
                                return false;
                        }
                        el.html('<div class="progress"><div class="progress-bar progress-bar-success progress-bar-striped active" style="width: 100%"></div></div>');
                    },
                    onComplete: function(file, response){                    
                        //Add uploaded file to list
                        if(response.status === "success"){
                            $(el.attr("data-target")).val(response.fileName);                                            
                            el.html('');
                            var list = $('<ul></ul>').appendTo(el).addClass('success');
                            $('<li></li>').appendTo(list).html('<img src="'+URL.getBaseAction(response.fileLocation)+'" alt="" />');                            
                            $('<li class="remove"></li>').appendTo(list).html('<i title="Remove" class="color-orange smaller-80 glyphicon glyphicon-remove hand"></i>');
                        } else {
                            alert(response.message);
                            el.html('<img class="upload" src="'+URL.getBaseAction('resource/img/no_image.png')+'" />');
                            reInitiateFileUpload(el);
                        }
                    }
                });
            }
        });
	}


	function reInitiateFileUpload(el) {

        new AjaxUpload(el.find('.upload'), {
            action: URL.getSiteAction('upload/index/'+el.attr("data-type")),
            name: 'attachment',
            responseType: 'json',
            onSubmit: function(file, ext){
                
                if (! (ext && /^(jpg|png|jpeg|gif)$/.test(ext))){ 
                // extension is not allowed
                        status.text('Only JPG, PNG or GIF files are allowed');
                        return false;
                }
                el.html('<div class="progress"><div class="progress-bar progress-bar-success progress-bar-striped active" style="width: 100%"></div></div>');
            },
            onComplete: function(file, response){
                //Add uploaded file to list
                if(response.status === "success"){
                    $(el.attr("data-target")).val(response.fileName);                                            
                    el.html('');
                    var list = $('<ul></ul>').appendTo(el).addClass('success');
                    $('<li></li>').appendTo(list).html('<img src="'+URL.getBaseAction(response.fileLocation)+'" alt="" />');                        
                    $('<li class="remove"></li>').appendTo(list).html('<i title="Remove" class="color-orange smaller-80 glyphicon glyphicon-remove hand"></i>');
                } else {
                    alert(response.message);
                    el.html('<img class="upload" src="'+URL.getBaseAction('resource/img/no_image.png')+'" />');
                    reInitiateFileUpload(el);
                }
            }
        });
	}