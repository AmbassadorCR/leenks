  function LinksListCtrl($scope, $http) {
    $scope.newLink = {title: ''};
    $scope.listLinks = function() {
      $http({method: 'GET', url: '/links'}).
          success(function(data, status, headers, config) {
              $scope.links = data.results;               
              $scope.view = './Partials/list.html'; 
          })
      };

      $scope.delete = function(id){
         $http({method: 'DELETE', url: '/links/'+id}).
          success(function(data, status, headers, config) {
              $scope.listLinks();
          })
      };
      

      $scope.edit = function(link){
         $http.put('/links/'+link.id, link).
          success(function(data, status, headers, config) {
              $scope.listLinks();
          })
      };

      $scope.create = function(){
         $http.post('/links/', $scope.newLink).
          success(function(data, status, headers, config) {
              $scope.listLinks();
          })
      }

      $scope.view = './Partials/list.html'; 
      $scope.listLinks();
  }
  LinksListCtrl.$inject = ['$scope', '$http'];