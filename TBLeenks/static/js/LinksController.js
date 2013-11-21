  function LinksListCtrl($scope, $http, $templateCache) {
    $scope.listLinks = function() {
      $http({method: 'GET', url: '/links', cache: $templateCache}).
          success(function(data, status, headers, config) {
              $scope.links = data.results;               
              $scope.view = './Partials/list.html'; 
          })
      }
      
      $scope.view = './Partials//list.html'; 
      $scope.listLinks();
  }
  LinksListCtrl.$inject = ['$scope', '$http', '$templateCache'];