% read error list
errors = {'femaleErrors','maleErrors'};
colors = {'red', 'blue'}

for i=1:2

	male = dlmread(errors{i});
	centers = -20:0.1:20



	% historgram 
	figure(1); [hMale, centers] = hist(male, centers ); 
	% Normalize so that the sum of the points
	normalizedCountsMale = hMale/ sum(hMale);

	hold on;
% 	remove parts outside -8:8
	numCenterPts = 120;
	plot(centers(numCenterPts:end-numCenterPts), normalizedCountsMale(numCenterPts:end-numCenterPts), 'Color',colors{i});


	hold on;


end


% post edit to add legend
xlabel('alignment error (in seconds)');
ylabel('occurence counts (normalized)');

hleg1 = legend('female','male');
set(hleg1,'Location', 'NorthEast');


