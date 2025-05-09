import bigfish.multistack as multistack
import pandas as pd
import numpy as np

class Quantify():
    
    def count_matrix(self, cell_masks: np.ndarray, spot_coordinates: np.ndarray):
        
        ndim = spot_coordinates.shape[1] 
        cell_results = multistack.extract_cell(
            cell_label= cell_masks,
            rna_coord=spot_coordinates,
            ndim=ndim
        )
        spot_counts_per_cell = {}
        for cell_info in cell_results:
            cell_id = cell_info['cell_id']
            spots_in_cell = cell_info['rna_coord']
            spot_count = spots_in_cell.shape[0] if spots_in_cell is not None else 0
            spot_counts_per_cell[cell_id] = spot_count
            
        df = pd.DataFrame.from_dict(spot_counts_per_cell, orient='index', columns=['spot_count'])
        df.index.name = 'cell_id'
        df = df.reset_index()
        return df
    
    


    def bin_colocalization(self, cell_masks: np.ndarray, spot_coordinates_g1: np.ndarray, spot_coordinates_g2: np.ndarray) -> pd.DataFrame:
        """
        Determines binary colocalization (presence of both gene spots) within each cell.

        Args:
            cell_masks (np.ndarray): A 2D or 3D numpy array where each element
                                    contains the integer ID of the cell it belongs to
                                    (0 for background).
            spot_coordinates_g1 (np.ndarray): A numpy array of shape (N, D) where N is
                                            the number of spots and D is the number
                                            of dimensions (e.g., 2 for 2D, 3 for 3D).
                                            Coordinates should be in pixel/voxel space.
            spot_coordinates_g2 (np.ndarray): A numpy array with the same shape as
                                            spot_coordinates_g1 for the second gene.

        Returns:
            pd.DataFrame: A DataFrame with colums, cell IDs and a
                        boolean column 'bin_coloc' indicating True if both
                        genes are present in the cell, False otherwise.
        """
 
        labs_g1 = []
        for pos in spot_coordinates_g1:
            labs_g1.append(cell_masks[pos[0], pos[1]])

        labs_g2 = []
        for pos in spot_coordinates_g2:
            labs_g2.append(cell_masks[pos[0], pos[1]])

        cell_ids_g1 =  np.array(labs_g1)
        cell_ids_g2 =  np.array(labs_g2)

        cells_with_g1 = set(cell_ids_g1)
        cells_with_g2 = set(cell_ids_g2)

        all_cell_ids = np.unique(cell_masks)
        all_cell_ids = all_cell_ids[all_cell_ids != 0]

        coloc_status = {}
        for cell_id in all_cell_ids:
                coloc_status[cell_id] = (cell_id in cells_with_g1) and (cell_id in cells_with_g2)

        df = pd.DataFrame.from_dict(coloc_status, orient='index', columns=['bin_coloc'])
        df.index.name = 'cell_id'
        df = df.reset_index()
        return df
