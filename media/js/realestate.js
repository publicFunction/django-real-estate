$(document).ready(function(){
    
    initOffices = function() {
        if ($('#contact-details').length) {
            var zoomLevel = 16;
            var edLatLng = new google.maps.LatLng(55.95386, -3.19936);
            var edMapOptions = {zoom: zoomLevel,
                                center: edLatLng,
                                mapTypeId: google.maps.MapTypeId.ROADMAP
                                }
            var edMap = new google.maps.Map(document.getElementById('office-location-edinburgh'), edMapOptions);
            var edmarker = new google.maps.Marker({
                                                    position: edLatLng,
                                                    map: edMap,
                                                    title: 'edinburgh office'
                                                });
                                                
            var glLatLng = new google.maps.LatLng(55.85979, -4.25096);
            var glMapOptions = {zoom: zoomLevel,
                                center: glLatLng,
                                mapTypeId: google.maps.MapTypeId.ROADMAP
                                }
            var glMap = new google.maps.Map(document.getElementById('office-location-glasgow'), glMapOptions);
            var glmarker = new google.maps.Marker({
                position: glLatLng,
                map: glMap,
                title: 'glasgow office'
            });                                    
        }
    }
    
    $('#search-tabs').tabs({
        selected: 0,
        select: function(event, ui) {
            
        },
        create : function(event, ui) {
            var url = location.href;
            var $livetab = $(this).tabs();
            if (url.search('type=let') >= 0) {
                $(this).tabs(
                    "option",
                    "selected",
                    0
                );
                $('div.commercial h1 span#type, div.residential h1 span#type').html('Rent');
            } else {
                $('div.commercial h1 span#type, div.residential h1 span#type').html('Buy');
            }
        }
    });
    
    $('#resi-tabs, #comm-tabs').tabs({
        selected: 0,
        select: function(event, ui) {
            var url = location.href;
            var $tabTextLive;
            var $tabTextDead;
            if(ui.index == 0) {
                $tabTextLive = $(this).closest('div').find('ul li:first-child a');
                $tabTextDead = $(this).closest('div').find('ul li:last-child a');
                $tabTextLive.html('Properties to Rent');
                $tabTextDead.html('Properties to Buy');
                $('div.commercial h1 span#type, div.residential h1 span#type').html('Rent');
                if(url.search('&type=let') >= 0 && url.search('&pgng=') <= -1) {
                    location.href = "residential&type=buy";
                }
            }
            if(ui.index == 1) {
                $tabTextLive = $(this).closest('div').find('ul li:last-child a');
                $tabTextDead = $(this).closest('div').find('ul li:first-child a');
                $tabTextLive.html('Properties to Buy');
                $tabTextDead.html('Properties to Rent');
                $('div.commercial h1 span#type, div.residential h1 span#type').html('Buy');
                if(url.search('&type=buy') >= 0 && url.search('&pgng=') <= -1) {
                    location.href = "residential&type=let";
                }
            }
        },
        create : function(event, ui) {
            var url = location.href;
            var $livetab = $(this).tabs();
            $(this).tabs(
                    "option",
                    "selected",
                    0
                );
            if (url.search('type=let') >= 0 || url.search('type=buy') <= 0) {
                $(this).tabs(
                    "option",
                    "selected",
                    0
                );
                $('div.commercial h1 span#type, div.residential h1 span#type').html('Rent');
            } else {
                $(this).tabs(
                    "option",
                    "selected",
                    1
                );
                $('div.commercial h1 span#type, div.residential h1 span#type').html('Buy');
            }
            if($('#comm-tabs').length) {
               var $searchTabs = $('#search-tabs');
               var $tabs = $searchTabs.find('li');
               $.each($tabs, function() {
                   var $childA = $(this).children('a');
                   $.each($childA, function() {
                       if($(this).attr('href') == '#search-resi') {
                           var $tab = $(this).parent('li');
                           $tab.hide();
                           $('#search-resi').hide();
                       }
                   });
               });
                $searchTabs.tabs(
                    "option",
                    "selected",
                    1
                );
           }
           if($('#resi-tabs').length) {
               var $searchTabs = $('#search-tabs');
               var $tabs = $searchTabs.find('li');
               $.each($tabs, function() {
                   var $childA = $(this).children('a');
                   $.each($childA, function() {
                       if($(this).attr('href') == '#search-comm') {
                           var $tab = $(this).parent('li');
                           $tab.hide();
                           $('#search-comm').hide();
                       }
                   });
               });
                $searchTabs.tabs(
                    "option",
                    "selected",
                    0
                );
           }

        }
    });
    
    /*$('#search-comm input#search-q, #search-resi input#search-q').autocomplete({
        source: function(req, resp) {
                    var searchURL = 'lib/search.php?q='+req.term;
                    $.getJSON(searchURL+'&callback=?', function(data) {
                        var locations = [];
                        $.each(data, function(i, loc) {
                            locations.push(loc)
                        });
                        resp(locations);
                    });
       },
       select: function(e, ui) {
           //var  locale = ui.item.value,
           //     span = $('<span>').text(locale);
           //     span.insertBefore('#results')
       },
       change: function() {

       }
    });*/
   
    $('#searchRes').live('click', function() {
       var $searchParam = $(this).closest('form').find('#search-q');
       var $searchChoice = $(this).closest('form').find('input[type=radio]').is(':checked');
       if($searchChoice) {
           return true;
       } else {
           alert('Please make a choice between buying or Renting/Letting!');
           return false;
       }
    });
   
    $('#menu li a').live('click', function() {
       var $links = $(this).closest('ul').find('a');
       $.each($links, function() {
           $(this).css({'color':'#000'});
       });
       location.href = $(this).attr('href');
    });
   
    $('#smallcheckboxbox input[type=radio]').live('click', function() {
       var $buy = $(this).closest('form').find('#price_buy');
       var $let = $(this).closest('form').find('#price_let');
       if($(this).attr('id')== "buy") {
           $buy.show();
           $let.hide();
       } else {
           $buy.hide();
           $let.show();
       }
    });
   
    if($('#smallcheckboxbox').length) {
        $.each($('#smallcheckboxbox input'), function() {
           if($(this).is(':checked')) {
               if($(this).attr('id') == "let") {
                   $('#price_buy').hide();
                   $('#price_let').show();
               } else {
                   $('#price_let').hide();
                   $('#price_buy').show();
               }
           }
        });
    }
    
    if($('#homepage-slider').length) {
        $('#homepage-slider').easySlider({
                                            controlsShow: false,
                                            continuous: true,
                                            auto: true,
                                            pause: 6000,
                                            speed : 1000
                                        });
    }
    
    if($('#smallnavi').length) {
        $('#smallnavi li a#return').live('click', function() {
            return true;
        });
    }
    
    if ($('#google-map-view').length) {
        loadMaps('showMap');
    } else {
        loadMaps('initOffices');
    }
    
    $('#iphone-app div#link a').live('click', function() {
        window.open($(this).attr('href'), 'app-popup');
        return false;
    });
    
    $('#search_term').live('keyup', function(evt) {
    	$.post('/ajax/getaddress/',{'term': $(this).val()}, function(response) {
    		var resp = $.parseJSON(response);
    		if (resp.status == 200) {
    			console.log(resp.data['test']);
    		}
    	});
    });
    
    
    highlightPage();
    
});

function loadMaps(callback) {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "http://maps.google.com/maps/api/js?sensor=false&callback="+callback;
  document.body.appendChild(script);
}    /*$('#search-comm input#search-q, #search-resi input#search-q').autocomplete({
        source: function(req, resp) {
                    var searchURL = 'lib/search.php?q='+req.term;
                    $.getJSON(searchURL+'&callback=?', function(data) {
                        var locations = [];
                        $.each(data, function(i, loc) {
                            locations.push(loc)
                        });
                        resp(locations);
                    });
       },
       select: function(e, ui) {
           //var  locale = ui.item.value,
           //     span = $('<span>').text(locale);
           //     span.insertBefore('#results')
       },
       change: function() {

       }
    });*/

function highlightPage() {
    var page = location.href;
    page = page.split('/');
    var splitCount = page.length-1;
    page = page[splitCount];
    if(page.search('&')) {
        page = page.split('&');
        page = page[0];
    }
    if(page.search('type')) {
        page = page.replace('?type=','_');
    }
    if (page == "" || page == null) {
        page = 'home';
    }
    $('li a#'+page).addClass('activeLink');
}
