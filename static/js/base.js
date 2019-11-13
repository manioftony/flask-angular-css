var app = angular.module('myApp',  ['ngRoute']);

app.config(function($interpolateProvider,$httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
});



app.config(function($routeProvider) {

    $routeProvider
    .when("/profile", {
        templateUrl : "/static/templates/one.html",
        controller: 'StudentController'

    })
    .when("/student", {
        templateUrl : "/static/templates/two.html",
        controller: 'ProfileController'

    })
});





app.controller('StudentController', function($scope,$http) {


            $scope.tableinfo = function(){
                $http.get("/api/profile/").then(function(response){
                    $scope.obj=response.data.data
                });
            }
            $scope.tableinfo()


});


app.controller('ProfileController', function($scope,$http) {

            $scope.tableinfo = function(){
                $http.get("/api/subject/").then(function(response){
                    $scope.obj=response.data.data
                });
            }
            $scope.tableinfo()



});