jQuery(function(jq){

    jq('#content').delegate(".kundart-socialpublisher form input", "click", (function(event){
        event.preventDefault();
        var form = jq(this).closest('form');
        var action = jq(this).attr('name');
       jq.ajax({
            type: 'POST',
            url: form.attr("action"),
            data: action + '=foo',
            beforeSend: function(msg){
                  if (action == 'form.twitter_post'){
                      jq("input[name=form.twitter_post]").removeClass('twitter-button');
                      jq("input[name=form.twitter_post]").addClass('request-loader');
                  } else {
                      jq("input[name=form.facebook_post]").removeClass('facebook-button');
                      jq("input[name=form.facebook_post]").addClass('request-loader');
                  }
            },

            success: function(data) {
                var response = jq.parseJSON(data);
                if (action == 'form.twitter_post'){
                    if (response['twitter_status'] == 1) {
                        jq("input[name=form.twitter_post]").removeClass('request-loader');
                        jq("input[name=form.twitter_post]").addClass('twitter-button-published');
                        jq("input[name=form.twitter_post]").val(jq('#published_on_twitter').val());
                        jq("input[name=form.twitter_post]").attr('disabled', true);
                    } else {
                        jq("input[name=form.twitter_post]").addClass('twitter-button');
                        alert(jq('#error_message').val());
                    }
                } else {
                    if (response['facebook_status'] == 1) {
                        jq("input[name=form.facebook_post]").removeClass('request-loader');
                        jq("input[name=form.facebook_post]").addClass('facebook-button-published');
                        jq("input[name=form.facebook_post]").val(jq('#published_on_facebook').val());
                        jq("input[name=form.facebook_post]").attr('disabled', true);


                    } else {
                        jq("input[name=form.facebook_post]").addClass('facebook-button');
                        alert(jq('#error_message').val());
                    }
                }
            }
        });

     }));    

});