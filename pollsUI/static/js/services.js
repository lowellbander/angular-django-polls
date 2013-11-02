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

services.factory('Polls', ['$resource', 
    //change this out to pull from django DB
    function ($resource) {
        return $resource('static/data-json/real.json');    
    }]);

// services.factory('Testing', ['$resource',
//     function ($resource) {
//         return $resource('http://0.0.0.0:8001/api/v1/poll/1/?format=json');
//     }]);


services.factory('Testing', ['$resource', '$http',
    function ($resource, $http) {
        return $resource('http://0.0.0.0:8001/api/v1/poll/1/?format=json',
            {}, {
                all: {
                    method: 'GET',
                    isArray: false,
                    transformResponse: tastypieDataTransformer($http)
                }
            });
    }]);

// services.factory('Task', ['$resource', '$log', '$http', 'taskURI',
//     function ($resource, $log, $http, taskURI) {
//         return $resource(taskURI+'/api/dev/task/:taskID?format=json',
//             {taskID:'@id'}, {
//                 all: {
//                     method: 'GET',
//                     isArray: true,
//                     transformResponse: tastypieDataTransformer($http)
//                 }
//             });
//     }]);