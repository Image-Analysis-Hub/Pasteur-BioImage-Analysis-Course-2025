import numpy as np

class Cleaning():
    def subsel_points_in_mask_fish(self, points: np.ndarray, mask_fish: np.ndarray) -> np.ndarray:
        """Chooses the points wich are in the mask_fish.

        Args:
            points (np.ndarray): detected spots, of dimension n.3 or n.2.
            mask_fish (np.ndarray): fish mask (2d).

        Returns:
            np.ndarray: selected points  (if points is of dimension n.3, the selected points will also be n.3) .
            np.ndarray: indexes of the selected points.
        """
        
        if np.shape(points)[1] == 2:
            sel_points = []
            indexes    = []
            for ind, point in enumerate(points):
                if mask_fish[point[0], point[1]]:
                    sel_points.append(point)
                    indexes.append(ind)
            sel_points = np.array(sel_points)
            indexes    = np.array(indexes)
            return sel_points, indexes
        elif np.shape(points)[1] == 3:
            sel_points = []
            indexes    = []
            for ind, point in enumerate(points):
                if mask_fish[point[1], point[2]]:
                    sel_points.append(point)
                    indexes.append(ind)      
            sel_points = np.array(sel_points)
            indexes    = np.array(indexes)  
            return sel_points, indexes