color_coords = [[75, 75, (200, 100, 10), 2], [75, 175, (200, 100, 10), 2], [75, 275, (200, 100, 10), 2], [75, 375, (200, 100, 10), 2], [75, 475, (200, 100, 10), 2], [75, 575, (200, 100, 10), 2], [75, 675, (200, 100, 10), 2], [175, 75, (200, 100, 10), 2], [175, 175, (200, 100, 10), 2], [175, 275, (200, 100, 10), 2], [175, 375, (200, 100, 10), 2], [175, 475, (200, 100, 10), 2], [175, 575, (200, 100, 10), 2], [175, 675, (200, 100, 10), 2], [275, 75, (200, 100, 10), 2], [275, 175, (200, 100, 10), 2], [275, 275, (255, 1, 255), 10], [275, 375, (255, 1, 255), 10], [275, 475, (255, 1, 255), 10], [275, 575, (255, 1, 255), 10], [275, 675, (255, 1, 255), 10], [375, 75, (200, 100, 10), 2], [375, 175, (200, 100, 10), 2], [375, 275, (255, 1, 255), 10], [375, 375, (255, 1, 255), 10], [375, 475, (255, 1, 255), 10], [375, 575, (255, 1, 255), 10], [375, 675, (255, 1, 255), 10], [475, 75, (200, 100, 10), 2], [475, 175, (200, 100, 10), 2], [475, 275, (255, 1, 255), 10], [475, 375, (255, 1, 255), 10], [475, 475, (200, 200, 1), 20], [475, 575, (200, 200, 1), 20], [475, 675, (200, 200, 1), 20], [575, 75, (200, 100, 10), 2], [575, 175, (200, 100, 10), 2], [575, 275, (255, 1, 255), 10], [575, 375, (255, 1, 255), 10], [575, 475, (200, 200, 1), 20], [575, 575, (200, 200, 1), 20], [575, 675, (200, 200, 1), 20], [675, 75, (200, 100, 10), 2], [675, 175, (200, 100, 10), 2], [675, 275, (255, 1, 255), 10], [675, 375, (255, 1, 255), 10], [675, 475, (200, 200, 1), 20], [675, 575, (200, 200, 1), 20], [675, 675, (1, 255, 1), 50]]
info = {
    
   'atlas': [(175, 25), 301],
   'backspacex': [(375, 25), 301],
   'ducati': [(575, 25), 301],
   'hepsi1': [(375, 725), 301],
   'mechrix': [(575, 725), 301],
   'meturoam': [(25, 575), 301],
   'nebula': [(175, 725), 301],
   'ohmygroup': [(25, 175), 301],
   'tulumba': [(25, 375), 301]
 
}

targetPoint = costFunction(info,Color_coords)
print(targetPoint)




def costFunction(info,Color_coords):
   
   my_loc = info['atlas'][0]
   enemy_loc = [info['backspacex'][0],info['ducati'][0],info['hepsi1'][0],info['mechrix'][0],info['meturoam'][0],info['nebula'][0],info['ohmygroup'][0],info['tulumba'][0]]
   
   my_point = info['atlas'][1]
   enemy_point = [info['backspacex'][1],info['ducati'][1],info['hepsi1'][1],info['mechrix'][1],info['meturoam'][1],info['nebula'][1],info['ohmygroup'][1],info['tulumba'][1]]

   chosen_Base_points = []

   chosen_Base = chooseNineBase(Color_coords,my_loc)
   
   for j in chosen_Base:
      for k in Color_coords:
         if j[0] == k[0] and j[1] == k[1]:
            chosen_Base_points.append(k[3])   


   targetPoints = []              # benim target pointlerimin arrayi 
   distanceCosts = []             # benim distanceCostlarım 
   pointCosts = []                # benim pointCostlarım
   myPointBlockages = []          # benim puan blokajların


   enemyDistanceCosts = []        # başkalarının distanceCostları
   enemyPointCosts = []           # başkalarının pointCostları
   enemyTargetPoints = []         # başkalarının targetPointleri

   costs = []


   for ind_i, i in enumerate(chosen_Base):

      targetPoints.append(targetDecider(i,my_loc))

      distanceCosts.append(distanceCost(targetPoints[ind_i],my_loc)) # kendi distance'ımız
      pointCosts.append(pointCost(chosen_Base_points[ind_i])) # kendi pointimiz
      sum_enemydistanceCost = 0
      sum_enemypointCost = 0
      for s in range(8):

         enemytargetPoints.append(targetDecider(i,enemy_loc[s])) # düşmanların target pointi 
         sum_enemydistanceCost = sum_enemydistanceCost + enemyDistanceCost(my_loc,enemy_loc[s],targetPoints[ind_i],enemytargetPoints[ind_i]) # düşmanların distance'ı (toplanacak)
         sum_enemypointCost = sum_enemypointCost + enemyPointCost(my_point,enemy_point[s]) 

      enemyDistanceCosts.append(sum_enemydistanceCost)
      enemyPointCosts.append(sum_enemypointCost)  
      myPointBlockages.append(myPointBlockage(my_point,chosen_Base_points[ind_i]))
      
      costs[ind_i] = (distanceCosts[ind_i] + pointCosts[ind_i] + enemyDistanceCosts[ind_i] + enemyPointCosts[ind_i] + myPointBlockages[ind_i]) / 6.4

   index = costs.index(min(costs))
   targetPoint = targetPoints[index]      


   return targetPoint 

def chooseNineBase(Color_coords,my_loc):
   
   Base_coords = []
   chosen_Base = []
   distances = []
   chosen_radii = 3
   colors = []

   for p in Color_coords:
      p.pop(2)
      colors.append(p.pop(2))
      Base_coords.append(p)
   
   
   for i in Base_coords: 
      if abs(i[0]-my_loc[0]) < 25 and abs(i[1]-my_loc[1]) < 25:
         Base_coords.remove(i)

   for j in Base_coords:
      a = ((j[0]-my_loc[0])**2 + ((j[1]-my_loc[1]))**2)**0.5
      distances.append(a)
   
   n = 0
   while (n < (chosen_radii**2)):
      u = min(distances)
      ind_u = distances.index(u)
      if colors[ind_u] == (1,1,1):
         distances.remove(u)
      else:   
         chosen_Base.append(Base_coords[ind_u])
         distances.remove(u)
         n = n+1

   return chosen_Base 

def targetDecider(Base_coord,my_loc):
   
   if Base_coord[0]-my_loc[0] > 25 and Base_coord[1]-my_loc[1] > 25:
   #region 1  
      targetPoint = (Base_coord[0]-25,Base_coord[1]-25)
      return targetPoint

   elif Base_coord[0]-my_loc[0] < -25 and Base_coord[1]-my_loc[1] > 25:
   #region 3  
      targetPoint = (Base_coord[0]+25,Base_coord[1]-25)  
      return targetPoint

   elif Base_coord[0]-my_loc[0] < -25 and Base_coord[1]-my_loc[1] < -25:
   #region 5  
      targetPoint = (Base_coord[0]+25,Base_coord[1]+25)
      return targetPoint  

   elif Base_coord[0]-my_loc[0] > 25 and Base_coord[1]-my_loc[1] < -25:
   #region 7  
      targetPoint = (Base_coord[0]-25,Base_coord[1]+25)
      return targetPoint

   elif abs(Base_coord[0]-my_loc[0]) < 25 and Base_coord[1]-my_loc[1] > 25:
   #region 2
      targetPoint = (my_loc[0],Base_coord[1]-25)
      return targetPoint

   elif abs(Base_coord[0]-my_loc[0]) < 25 and Base_coord[1]-my_loc[1] < -25:
   #region 6
      targetPoint = (my_loc[0],Base_coord[1]+25) 
      return targetPoint

   elif Base_coord[0]-my_loc[0] > 25 and abs(Base_coord[1]-my_loc[1]) < 25:
   #region 8
      targetPoint = (Base_coord[0]-25,my_loc[1])
      return targetPoint 

   elif Base_coord[0]-my_loc[0] < -25 and abs(Base_coord[1]-my_loc[1]) < 25:
   #region 4
      targetPoint = (Base_coord[0]+25,my_loc[1]) 
      return targetPoint   
   else:
 
      pass  
def distanceCost(targetPoint, my_loc):  #9 kere çağırılacak
   
   C_1 = 2
   distance = ((targetPoint[0]-my_loc[0])**2+(targetPoint[1]-my_loc[1])**2)**0.5
   A_1 = abs((100-(100-distance))/100)**1.5
   return A_1*C_1

def pointCost(point):     #9 kere çağırılacak
   
   C_2 = 2.5
   max_point = 100
   A_2 = ((max_point-point)/max_point)**3
   return A_2*C_2

def enemyDistanceCost(my_loc,enemy_loc,my_targetPoint,enemy_targetPoint):  #36 kere çağırılacak 
   
   C_3 = 1.5
   my_distance = ((my_targetPoint[0]-my_loc[0])**2+(my_targetPoint[1]-my_loc[1])**2)**0.5
   enemy_distance = ((enemy_targetPoint[0]-enemy_loc[0])**2+(enemy_targetPoint[1]-enemy_loc[1])**2)**0.5 
   if my_distance - enemy_distance <= 5:
     A_3 = 0.05
   elif my_distance - enemy_distance <= 10 and my_distance - enemy_distance >= 5:
     A_3 = 0.08
   elif my_distance - enemy_distance <= 15 and my_distance - enemy_distance >= 10:
     A_3 = 0.16
   elif my_distance - enemy_distance <= 20 and my_distance - enemy_distance >= 15:
     A_3 = 0.30
   elif my_distance - enemy_distance <= 25 and my_distance - enemy_distance >= 20:
     A_3 = 0.49
   elif my_distance - enemy_distance <= 30 and my_distance - enemy_distance >= 25:
     A_3 = 0.69
   elif my_distance - enemy_distance <= 50 and my_distance - enemy_distance >= 30:
     A_3 = 0.85
   elif my_distance - enemy_distance >= 50:
     A_3 = 0.99
   else:
     A_3 = 0.00001   
   return A_3*C_3    

def enemyPointCost(my_point,enemy_point):  #36 kere çağırılacak 

   C_4 = 0.4
   if enemy_point < my_point:
     A_4 = 0.001
   else:
     A_4 = 0.05
   return A_4*C_4

def myPointBlockage(my_point,point):

   if point > my_point:
     A_5 = 1000
   else:
     A_5 = 0
   return A_5
