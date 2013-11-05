'use strict';

/* Controllers */

var controllers = angular.module('app.controllers', []);

controllers.controller('VoteCtrl', ['$scope', '$http', '$routeParams', 'Options',
    function ($scope, $http, $routeParams, Options) {
        $scope.optionData = Options.get(function(){
            $scope.options = $scope.optionData['objects']
        });
    }]);

controllers.controller('PollCtrl', ['$scope', '$http', 'Polls',
    function ($scope, $http, Polls) {
        $scope.pollData = Polls.get(function(){
            $scope.polls = $scope.pollData['objects']
        });
        $scope.testVal = 'asd';
        var tester = function(){
            $scope.testVal = 'WOOT';
        };
    }]);

/////////////////////////////////
// Vestigial Beyond This Point //
/////////////////////////////////

controllers.controller('NavbarCtrl', ['$scope', '$http', '$location', 'Session',
    function ($scope, $http, $location, Session) {
        $scope.session = Session.session;
        $scope.logout = Session.logout;
        $scope.login = function () {
            Session.login($scope.username, $scope.password);
        };

        $scope.isNavbarActive = function (navBarPath) {
            return navBarPath === $location.path();
        };

        $scope.hasPendingRequests = function () {
            return $http.pendingRequests.length > 0;
        };
    }]);

var ModalInstanceCtrl = function ($scope, $modalInstance, task) {
    $scope.task = task;

    $scope.save = function () {
        $modalInstance.close($scope.task);
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
};