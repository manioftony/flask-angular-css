var app = angular.module('myApp', ['ui.router']);

app.config(function($interpolateProvider, $httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
});


app.config(function ($stateProvider, $urlRouterProvider){






    $urlRouterProvider.otherwise("/")

    $stateProvider.state("student", {
        url: "",
        templateUrl: "/static/templates/one.html",
        controller: "StudentController"
      }).state("profile", {
        url: "",
        templateUrl: "/static/templates/two.html",
        controller: "ProfileController"
      });
});



app.controller( "StudentController", function($scope,$http) {

            $scope.tableinfo = function(){
                $http.get("/api/profile/").then(function(response){
                    $scope.obj=response.data.data
                });
            }
            $scope.tableinfo()


})


app.controller( "ProfileController", function($scope,$http) {


            $scope.tableinfo = function(){
                $http.get("/api/subject/").then(function(response){
                    $scope.obj=response.data.data
                });
            }
            $scope.tableinfo()




})