class Solution:
    def trap(self, height: List[int]) -> int:

        dim = len(height)
        left_bound = 0
        right_bound = dim-1

        # get the starting left pointer
        while left_bound+1 < dim and height[left_bound]<=height[left_bound+1]:
            left_bound+=1
        # get the starting right pointer
        while right_bound - 1 >=0 and height[right_bound]<=height[right_bound-1]:
            right_bound-=1

        left = left_bound
        right = right_bound

        print(left, right)

        s = set()

        while left < right:
            if height[left] <= height[left+1]:
                left += 1
            else:
                r = left + 1 
                while r<right and height[r]<height[left]:
                    r+=1
                if height[left] <= height[r]:
                    s.add((left, r))
                left = r

        left = left_bound
        right = right_bound

        while left < right:
            if height[right] <= height[right-1]:
                right -= 1
            else:
                l = right - 1 
                while l>left and height[l]<height[right]:
                    l-=1
                if height[l] >= height[right]:
                    s.add((l, right))
                right = l
        
        water = 0
        for couple in s:
            left = couple[0]
            right = couple[1]

            blocks = 0
            for i in range(left+1, right):
                blocks += height[i]
            water += -blocks + (right-left-1)*min(height[left], height[right])

        return water