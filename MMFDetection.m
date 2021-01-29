%%
%   MMF 
%   Fiber length vs Q factor
%   Fiber length vs Optical power
%
% 
%
%%

clear functions
clear all
close all
%% SIMULATION
%fibra OM4(0.8db/km)@1300nm
comprimento=[0.1, 0.5, 1, 1.5, 2, 2.5, 3];
q_factor_4=[9.39, 8.51, 7.52, 7.16, 6.28, 4.58, 3.13];
optical_pw_4=[-18, -18.41, -18.76, -19.22, -19.46, -19.55, -21];

%fibra OM3(1.5db/Km)@1300nm
q_factor_3=[9.25, 7.87, 6.06, 5.63, 4.74, 3.60, 2.36];
optical_pw_3=[-18.16, -18.76, -19.46, -20.27, -20.86, -21.30, -23];

%fibra OM2 (1.2db/km) @1300nm
q_factor_2=[9.31, 8.14, 6.43, 6.25, 5.36, 4.02, 2.60];
optical_pw_2=[-18.13, -18.61, -19.16, -19.82, -20.2, -20.4, -22];

%fibra OM1 (1db/km)@1300nm
q_factor_1=[9.35, 8.32, 6.68, 6.68, 5.80, 4.30, 2.80];
optical_pw_1=[-18.11, -18.51, -18.96, -19.56, -19.86, -20.05, -22.03];


%% PLOTS
%MMF LENGTH VS QFACTOR
figure(1)
plot(comprimento,q_factor_4,'Linewidth',1,'color','r');
hold on
grid on
plot(comprimento,q_factor_3,'Linewidth',1,'color','b');
plot(comprimento,q_factor_2,'Linewidth',1);
plot(comprimento,q_factor_1,'Linewidth',1);
title('MMF length vs Q-factor');
legend('MMF 4 (0.8 db/Km)','MMF 3 (1.5 db/Km)','MMF 2 (1.2 db/Km)','MMF 1 (1 db/Km)','Location','SouthWest')
xlabel('Length(Km)'), ylabel('Q Factor');
axis([0.1 3 0 10]);

%%
%MMF LENGTH VS Optical Power received
figure(2)
%subplot(211)
plot(comprimento,optical_pw_4,'Linewidth',1,'color','r');
hold on
grid on
plot(comprimento,optical_pw_3,'Linewidth',1,'color','b');
plot(comprimento,optical_pw_2,'Linewidth',1);
plot(comprimento,optical_pw_1,'Linewidth',1);
title('MMF length vs Optical power received ');
legend('MMF 4 (0.8 db/Km)','MMF 3 (1.5 db/Km)','MMF 2 (1.2 db/Km)','MMF 1 (1 db/Km)','Location','NorthEast')
xlabel('Length(Km)'), ylabel('Optical Power(dbm)');
axis([0.1 3 -22 -17]);

%Optical power received vs Qfactor
figure(3)
plot(optical_pw_4, q_factor_4,'Linewidth',1,'color','r');
hold on
grid on
plot(optical_pw_3, q_factor_3,'Linewidth',1,'color','b');
plot(optical_pw_2, q_factor_2,'Linewidth',1);
plot(optical_pw_1, q_factor_1,'Linewidth',1);
title('Optical received power vs Qfactor ');
legend('MMF 4 (0.8 db/Km)','MMF 3 (1.5 db/Km)','MMF 2 (1.2 db/Km)','MMF 1 (1 db/Km)','Location','NorthWest')
xlabel('Optical Power(dbm)'), ylabel('Q factor');
axis([-23 -18 2 10 ]);

