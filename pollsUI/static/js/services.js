'use strict';

//http://docs.angularjs.org/tutorial/step_11
//http://docs.angularjs.org/api/ngResource.$resource

/* Services */
var services = angular.module('app.services', ['ngResource']);

services.value('version', '0.1');

var tastypieDataTransformer = function ($http) {
    return $http.defaults.transformResponse.concat([
        function (data, headersGetter) {
            var result = data.objects;
            result.meta = data.meta;
            return result;
        }
    ])
};

//////////////////////////
/// Lowell's Additions ///
//////////////////////////

services.factory('Choices', ['$resource',
    //change this out to pull from django DB
    function ($resource) {
        return $resource('static/data-json/array.json');
}]);

services.factory('Polls', ['$resource', '$http', 'pollsURI',
    function ($resource, $http, pollsURI) {
        return $resource(pollsURI + '/api/v1/poll/',
            {}, {
                all: {
                    method: 'GET',
                    isArray: false,
                    transformResponse: tastypieDataTransformer($http)
                }
            });
    }]);

services.factory('Options', ['$resource', '$http', 'pollsURI',
    function ($resource, $http, pollsURI) {
        return $resource(pollsURI + '/api/v1/option/?id=2',
            {}, {
                all: {
                    method: 'GET',
                    isArray: false,
                    transformResponse: tastypieDataTransformer($http)
                }
            });
    }]);

// services.factory('Options1', ['$resource', '$http', 'pollsURI',
//     function ($resource, $http, pollsURI) {
//         return $resource(pollsURI + '/api/v1/option/set/1;3/?format=json',
//             {}, {
//                 all: {
//                     method: 'GET',
//                     isArray: false,
//                     transformResponse: tastypieDataTransformer($http)
//                 }
//             });
//     }]);

// services.factory('Options1', ['$resource', '$http', 'pollsURI',
//     function ($resource, $http, pollsURI) {
//         return $resource(pollsURI + '/api/v1/option/set/4;6/?format=json',
//             {}, {
//                 all: {
//                     method: 'GET',
//                     isArray: false,
//                     transformResponse: tastypieDataTransformer($http)
//                 }
//             });
//     }]);