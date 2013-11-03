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

services.factory('Polls', ['$resource', '$http',
    function ($resource, $http) {
        return $resource('http://0.0.0.0:8003/api/v1/poll/?format=json',
            {}, {
                all: {
                    method: 'GET',
                    isArray: false,
                    transformResponse: tastypieDataTransformer($http)
                }
            });
    }]);