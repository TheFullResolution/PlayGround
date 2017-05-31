/* global google, ko */

var markers = {
    "main": {
        "name": "The Next Web",
        "street": "Frederiksplein 42",
        "postCode": "1017 XN",
        "city": "Amsterdam",
        "country": "Netherlands"
    },
    "sections": [
        {
            "name": "Coffe Places",
            "answer": "I need coffee!",
            "places": [
                {
                    "name": "Frederix Micro Roasters",
                    "street": "Frederiksplein 29",
                    "postCode": "1017 XL"
                },
                {
                    "name": "Koffie Salon Centrum B.V.",
                    "street": "Utrechtsestraat 130-BG",
                    "postCode": "1017 VT"
                },
                {
                    "name": "Café Kale B.V.",
                    "street": "Weteringschans 267",
                    "postCode": "1017 XJ"
                }
            ]
        },
        {
            "name": "Supermarkets",
            "answer": "I need some groceries...",
            "places": [
                {
                    "name": "AH Frederiksplein",
                    "street": "Frederiksplein 1",
                    "postCode": "1017 XK"
                },
                {
                    "name": "Lidl",
                    "street": "Hemonylaan 25A",
                    "postCode": "1074 BJ"
                },
                {
                    "name": "AH Stadhouderskade",
                    "street": "Stadhouderskade 101D",
                    "postCode": "1073 AW"
                },
                {
                    "name": "Ekoplaza Stadhouderskade",
                    "street": "Stadhouderskade 94",
                    "postCode": "1073 AX"
                }
            ]},
        {
            "name": "ATMs",
            "answer": "I need cash.",
            "places": [
                {
                    "name": "Rabobank",
                    "street": "Weteringschans 275",
                    "postCode": "1017 XJ"
                },
                {
                    "name": "ABN AMRO Bank",
                    "street": "Stadhouderskade 123",
                    "postCode": "1074 AV"
                },
                {
                    "name": "AH Frederiksplein",
                    "street": "Frederiksplein 1",
                    "postCode": "1017 XK"
                }

            ]},
        {
            "name": "Lunch Spots",
            "answer": "I am hungry..",
            "places": [
                {
                    "name": "Bistrot des Alpes",
                    "street": "Utrechtsedwarsstraat 141",
                    "postCode": "1017 WE"
                },
                {
                    "name": "Il Boccalino",
                    "street": "Utrechtsestraat 133",
                    "postCode": "1017 VM"
                },
                {
                    "name": "Café de Huyschkaemer",
                    "street": "Utrechtsestraat 137",
                    "postCode": "1017 VM"
                },
                {
                    "name": "Uliveto Alimentari",
                    "street": "Weteringschans 118",
                    "postCode": "1017 XT"
                }
            ]},
        {
            "name": "Pubs",
            "answer": "Time for drinks!",
            "places": [
                {
                    "name": "Café Slijterij Oosterling",
                    "street": "Utrechtsestraat 140",
                    "postCode": "1017 VT"
                },
                {
                    "name": "Café de Huyschkaemer",
                    "street": "Utrechtsestraat 137",
                    "postCode": "1017 VM"
                },
                {
                    "name": "Café Kale B.V.",
                    "street": "Weteringschans 267",
                    "postCode": "1017 XJ"
                },
                {
                    "name": "Cafe Bouwman",
                    "street": "Utrechtsestraat 102",
                    "postCode": "1017 VS"
                }
            ]}]
};

var Section = function (data) {
    var self = this;
    this.name = ko.observable(data.name);
    this.answer = ko.observable(data.answer);

    this.placeList = ko.observableArray([]);
    data.places.forEach(function (placeItem) {
        self.placeList.push(new Place(placeItem));
    });

    this.showList = ko.observable(false);

    this.toggleList = function () {
        self.showList(!self.showList());
       
};
};




var Place = function (data,map) {
    var self = this;
    
    
    this.name = ko.observable(data.name);
    this.street = ko.observable(data.street);
    this.postCode = ko.observable(data.postCode);
    
    this.address = data.name + ',' + data.street + ',' + markers.main.city;
      
      markPlaces(this.address); 

    
};


var ViewModel = function () {
    var self = this;
    
    this.sectionList = ko.observableArray([]);

    markers.sections.forEach(function (sectionItem) {
        self.sectionList.push(new Section(sectionItem));
    });

    this.totalPlaceList = [];

    markers.sections.forEach(function (sectionItem) {
        sectionItem.places.forEach(function (placeItem) {
            self.totalPlaceList.push(placeItem);
        });
    });


    //List display *********************************************

    this.showList = ko.observable(false);

    this.toggleList = function () {
        self.showList(!self.showList());
    };

    this.listX = function () {
        ko.utils.arrayForEach(self.sectionList(), function (sectionItem) {
            sectionItem.showList(false);
        });
        self.showList(false);
    };

    //Search Area **********************************************

    this.searchQuery = ko.observable('');

    this.isSelected = ko.observable(false);

    this.emptySearch = function () {
        self.searchQuery('');
    };

    this.setIsSelected = function () {
        this.isSelected(true);
    };


    this.displayTotalList = ko.computed(function () {
        var search = self.searchQuery().toLowerCase();
        return ko.utils.arrayFilter(self.totalPlaceList, function (place) {
            return place.name.toLowerCase().indexOf(search) >= 0;
        });
    }, self);

};

ko.bindingHandlers.fadeVisible = {
    init: function (element, valueAccessor) {
        // Initially set the element to be instantly visible/hidden depending on the value
        var value = valueAccessor();
        $(element).toggle(ko.unwrap(value)); // Use "unwrapObservable" so we can handle values that may or may not be observable
    },
    update: function (element, valueAccessor) {
        // Whenever the value subsequently changes, slowly fade the element in or out
        var value = valueAccessor();
        ko.unwrap(value) ? $(element).slideToggle("slow") : $(element).fadeOut();
    }
};












var geocoder;

var map;

var initMap = function()  {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: {lat: 52.36, lng: 4.8989}
    });
    geocoder = new google.maps.Geocoder();
 
    geocodeAddress();
    ko.applyBindings(new ViewModel(map));
};


var geocodeAddress = function () {
var hq = markers.main.name + ',' + markers.main.street + ',' + markers.main.city;
    geocoder.geocode({'address': hq}, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            var logo = 'img/tnw-logo_1.svg';
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location,
                animation: google.maps.Animation.DROP,
                icon: logo
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
};



var markPlaces = function (adress) {
       geocoder.geocode({'address': adress}, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
              var p = results[0].geometry.location;
              var lat=p.lat();
              var lng=p.lng();
            marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location,
                animation: google.maps.Animation.DROP
                
            });
     console.log(adress);
    console.log(lat);
    console.log(lng);
        } else {
              // === if we were sending the requests to fast, try this one again and increase the delay
              if (status === google.maps.GeocoderStatus.OVER_QUERY_LIMIT) {
                  setTimeout(function(){markPlaces(adress)},delay);
              } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }}
    

    
    });
};


var delay = 150;
